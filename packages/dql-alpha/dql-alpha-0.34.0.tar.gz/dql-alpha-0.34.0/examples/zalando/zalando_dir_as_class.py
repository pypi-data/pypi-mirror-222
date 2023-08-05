"""
UDF to create 'class' and 'type' signals from the directory structure.
"""
from pathlib import Path

from sqlalchemy import Text
from tabulate import tabulate

from dql.query import C, DatasetQuery, udf


@udf((("class", Text), ("type", Text)), (C.parent,))
def dir_as_class(parent):
    try:
        s_class, s_type = Path(parent).parts[-2:]
    except ValueError:
        return ("", "")
    return (s_class, s_type)


if __name__ == "__main__":
    #   - save as a new shadow dataset
    DatasetQuery(path="s3://dql-zalando-hd-resized/zalando-hd-resized").filter(
        C.name.glob("*.jpg")
    ).add_signals(dir_as_class).save("zalando-with-signals")

    # Output the contents of the new dataset.
    print(tabulate(DatasetQuery(name="zalando-with-signals").results()[:10]))
