from __future__ import annotations

from typing import Any, Type

import pandas as pd

from minto.containers.base import Container
from minto.containers.records import Record


class Table(Container):
    """Data structure that maps data onto a `pandas.DataFrame`.

    This class is one of Container. The element in the each cell is a DataNode.
    Table class extends the basic functionality of a `pandas.DataFrame` with the ability to store and manipulate `DataNode` objects.

    Attributes:
        data (pd.DataFrame): The actual data stored in the table.
        name (tp.Hashable): The name of the Table, which is used as an identifier.
    """

    def __init__(self, schema: dict[str, Type[Any]]) -> None:
        super().__init__(schema)

        self._data = pd.DataFrame(columns=self.pandas_dtypes).astype(self.pandas_dtypes)

    def __getitem__(self, i: int) -> pd.Series[Any]:
        return self.data.iloc[i]

    @property
    def data(self) -> pd.DataFrame:
        return self._data

    def insert(self, record: Record | pd.Series[Any] | list[Any]) -> None:
        """Insert a new record to the Table.

        Args:
            record (Record): The data to be appended.
        """

        record = self._validate_record(record)

        if isinstance(record, Record):
            record = record.series()
        elif isinstance(record, list):
            record = pd.Series(record, index=self.schema)

        self._data.loc[len(self)] = record
        self._data = self._data.astype(self.pandas_dtypes)
