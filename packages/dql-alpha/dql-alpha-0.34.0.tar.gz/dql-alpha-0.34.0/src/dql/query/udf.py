from abc import ABC, abstractmethod
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from dql.catalog import Catalog

from .schema import Column, Object

if TYPE_CHECKING:
    from dql.dataset import DatasetRow

UDFType = Callable[["Catalog", "DatasetRow"], Any]

ColumnType = Any

# Specification for the output of a UDF, a sequence of tuples containing
# the column name and the type.
UDFOutputSpec = Sequence[Tuple[str, ColumnType]]


class BatchingStrategy(ABC):
    """BatchingStrategy provides means of batching UDF executions."""

    def __init__(self, signal_names):
        self.signal_names = signal_names

    @abstractmethod
    def __call__(
        self, func: Callable, params: Tuple[int, Sequence[Any]]
    ) -> Optional[List[Dict[str, Any]]]:
        """Apply the provided parameters to the UDF."""

    @abstractmethod
    def finalize(self, func: Callable) -> Optional[List[Dict[str, Any]]]:
        """Execute the UDF with any parameter sets stored."""

    def _process_results(
        self, row_ids: List[int], results: Sequence[Sequence[Any]]
    ) -> List[Dict[str, Any]]:
        """Create a list of dictionaries representing UDF results."""
        r = []
        for row_id, result in zip(row_ids, results):
            signals = {
                signal_name: signal_value
                for (signal_name, signal_value) in zip(self.signal_names, result)
            }
            r.append(dict(id=row_id, **signals))
        return r


class NoBatching(BatchingStrategy):
    """
    NoBatching implements the default batching strategy, which is not to
    batch UDF calls.
    """

    def __call__(
        self, func: Callable, params: Tuple[int, Sequence[Any]]
    ) -> Optional[List[Dict[str, Any]]]:
        (row_id, udf_params) = params
        return self._process_results([row_id], [func(*udf_params)])

    def finalize(self, func: Callable) -> Optional[List[Dict[str, Any]]]:
        return None


class Batch(BatchingStrategy):
    """
    Batch implements UDF call batching, where each execution of a UDF
    is passed a sequence of multiple parameter sets.
    """

    def __init__(self, count: int, signal_names: List[str]):
        super().__init__(signal_names)
        self.count = count
        self.batch: List[Sequence[Any]] = []

    def __call__(
        self, func: Callable, params: Tuple[int, Sequence[Any]]
    ) -> Optional[List[Dict[str, Any]]]:
        self.batch.append(params)
        if len(self.batch) >= self.count:
            batch, self.batch = self.batch[: self.count], self.batch[self.count :]
            row_ids, params = tuple(zip(*batch))
            results = func(params)
            return self._process_results(row_ids, results)
        return None

    def finalize(self, func: Callable) -> Optional[List[Dict[str, Any]]]:
        if self.batch:
            row_ids, params = tuple(zip(*self.batch))
            self.batch.clear()
            results = func(params)
            return self._process_results(row_ids, results)
        return None


def udf(
    output: UDFOutputSpec,
    parameters: Sequence[Union["Column", "Object"]],
    batch: int = 1,
):
    """Decorate a function to be usable as a UDF."""

    def decorator(func: Callable):
        return UDFBase(func, output, parameters, batch)

    return decorator


class UDFBase:
    """A base class for implementing stateful UDFs."""

    def __init__(
        self,
        func: Callable,
        output: UDFOutputSpec,
        parameters: Sequence[Union["Column", "Object"]],
        batch: int = 1,
    ):
        self.func = func
        self.parameters = parameters
        self.output = output
        signal_names = [signal_name for (signal_name, _) in output]

        self.batching: BatchingStrategy
        if batch == 1:
            self.batching = NoBatching(signal_names)
        elif batch > 1:
            self.batching = Batch(batch, signal_names)
        else:
            raise ValueError(f"invalid batch size {batch}")

    def __call__(
        self, catalog: "Catalog", row: "DatasetRow"
    ) -> Optional[List[Dict[str, Any]]]:
        params = []
        for p in self.parameters:
            if isinstance(p, Column):
                params.append(row[p.name])
            elif isinstance(p, Object):
                with catalog.open_object(row) as f:
                    obj: Any = p.reader(f)
                params.append(obj)
            else:
                raise ValueError("unknown udf parameter")
        signals = self.batching(self.func, (row.id, params))
        return signals

    def finalize(self) -> Optional[List[Dict[str, Any]]]:
        """
        Execute the UDF with any parameter sets still held by
        the batching strategy.
        """
        return self.batching.finalize(self.func)


def generator(*parameters: Union["Column", "Object", Type["Catalog"]]):
    def decorator(func: Callable):
        return Generator(func, *parameters)

    return decorator


class Generator:
    """A wrapper class for UDFs used to generate new dataset rows."""

    def __init__(
        self, func: Callable, *parameters: Union["Column", "Object", Type["Catalog"]]
    ):
        self.func = func
        self.parameters = parameters

    def __call__(self, catalog: "Catalog", row: "DatasetRow"):
        params = []
        for p in self.parameters:
            if isinstance(p, Column):
                params.append(row[p.name])
            elif isinstance(p, Object):
                with catalog.open_object(row) as f:
                    obj: Any = p.reader(f)
                params.append(obj)
            elif p is Catalog:
                params.append(catalog)
            else:
                raise ValueError("unknown udf parameter")
        yield from self.func(row, *params)
