from typing import List, Optional

from dql.catalog import Catalog, get_catalog
from dql.dataset import DatasetRow
from dql.query import DatasetQuery


class DataView:
    def __init__(
        self,
        contents: List[DatasetRow],
        reader,
        transform,
        catalog: Optional[Catalog] = None,
        client_config=None,
    ):
        self.contents = contents
        self.reader = reader
        self.transform = transform
        if catalog is None:
            catalog = get_catalog()
        self.catalog = catalog
        self.client_config = client_config or {}

    @classmethod
    def from_dataset(
        cls,
        name: str,
        reader,
        transform,
        num_workers: Optional[int] = None,
        worker_id: int = 0,
        *,
        catalog=None,
        client_config=None
    ):
        if num_workers is not None:
            query = DatasetQuery(name=name, catalog=catalog).chunk(
                worker_id, num_workers
            )
            return cls.from_query(
                query, reader, transform, catalog=catalog, client_config=client_config
            )
        if catalog is None:
            catalog = get_catalog()
        contents = list(catalog.ls_dataset_rows(name))
        return cls(contents, reader, transform, catalog, client_config)

    @classmethod
    def from_query(cls, query, reader, transform, *, catalog=None, client_config=None):
        if catalog is None:
            catalog = get_catalog()
        contents = query.results(row_factory=DatasetRow.from_result_row)
        return cls(contents, reader, transform, catalog, client_config)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, i):
        row = self.contents[i]
        with self.catalog.open_object(row, **self.client_config) as f:
            sample = self.reader(f)
        return self.transform(row, sample)
