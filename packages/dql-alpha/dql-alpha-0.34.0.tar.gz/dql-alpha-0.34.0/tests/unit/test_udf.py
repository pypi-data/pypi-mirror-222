from sqlalchemy import Integer

from dql.dataset import DatasetRow
from dql.query import C, UDFBase, generator, udf


def test_udf_single_signal():
    @udf((("mul", Integer),), (C.id, C.size))
    def t(a, b):
        return (a * b,)

    row = DatasetRow(
        id=6,
        vtype="",
        dir_type=1,
        parent="",
        name="obj",
        checksum="",
        parent_id=None,
        last_modified=None,
        anno={},
        etag="",
        version="",
        is_latest=True,
        size=7,
        owner_name="",
        owner_id="",
        source="",
        random=1234,
        location=None,
    )
    result = t(None, row)  # pylint: disable=no-value-for-parameter
    assert result[0]["mul"] == (42)


def test_udf_multiple_signals():
    @udf((("mul", Integer), ("sum", Integer)), (C.id, C.size))
    def t(a, b):
        return (a * b, a + b)

    row = DatasetRow(
        id=6,
        vtype="",
        dir_type=1,
        parent="",
        name="obj",
        checksum="",
        parent_id=None,
        last_modified=None,
        anno={},
        etag="",
        version="",
        is_latest=True,
        size=7,
        owner_name="",
        owner_id="",
        source="",
        random=1234,
        location=None,
    )
    result = t(None, row)  # pylint: disable=no-value-for-parameter
    assert result[0] == {"id": 6, "mul": 42, "sum": 13}


def test_generator():
    @generator(C.name)
    def gen(parent, name):
        yield parent, name

    row = DatasetRow(
        id=6,
        vtype="",
        dir_type=1,
        parent="",
        name="obj",
        checksum="",
        parent_id=None,
        last_modified=None,
        anno={},
        etag="",
        version="",
        is_latest=True,
        size=7,
        owner_name="",
        owner_id="",
        source="",
        random=1234,
        location=None,
    )

    assert list(gen(None, row)) == [(row, "obj")]


def test_udf_batching():
    @udf((("mul", Integer),), (C.id, C.size), batch=4)
    def t(vals):
        result = [(a * b,) for (a, b) in vals]
        return result

    inputs = list(zip(range(1, 11), range(21, 31)))
    results = []
    for size, row_id in inputs:
        row = DatasetRow(
            id=row_id,
            vtype="",
            dir_type=1,
            parent="",
            name="obj",
            checksum="",
            parent_id=None,
            last_modified=None,
            anno={},
            etag="",
            version="",
            is_latest=True,
            size=size,
            owner_name="",
            owner_id="",
            source="",
            random=1234,
            location=None,
        )
        result = t(None, row)  # pylint: disable=too-many-function-args
        if result:
            assert len(result) == 4  # Matches batch size.
            results.extend(result)

    # Not all the results have been retrieved yet, since the batch
    # size is not a multiple of the input count.
    assert len(results) < len(inputs)
    # Finalize the UDF.
    results.extend(t.finalize() or [])
    assert len(results) == len(inputs)
    assert results == [{"id": b, "mul": a * b} for (a, b) in inputs]


def test_stateful_udf():
    class MyUDF(UDFBase):
        def __init__(self, constant):
            super().__init__(self.sum, (("sum", Integer),), (C.size,))
            self.constant = constant

        def sum(self, size):
            return (self.constant + size,)

    udf_inst = MyUDF(5)
    inputs = range(1, 11)
    results = []
    for size in inputs:
        row = DatasetRow(
            id=5,
            vtype="",
            dir_type=1,
            parent="",
            name="obj",
            checksum="",
            parent_id=None,
            last_modified=None,
            anno={},
            etag="",
            version="",
            is_latest=True,
            size=size,
            owner_name="",
            owner_id="",
            source="",
            random=1234,
            location=None,
        )
        results.extend(udf_inst(None, row))

    assert len(results) == len(inputs)
    assert results == [{"id": 5, "sum": 5 + size} for size in inputs]
