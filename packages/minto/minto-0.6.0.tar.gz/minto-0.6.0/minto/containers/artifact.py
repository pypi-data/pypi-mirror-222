from __future__ import annotations

from typing import Any, Type

import pandas as pd

from minto.containers.base import Container, Record
from minto.typing import ArtifactDataType


class Artifact(Container):
    """Data structure that maps data onto a `dict`.

    Attributes:
        data (ArtifactDataType): The data stored in the Artifact.
        name (Hashable): The name of the Artifact. Defaults to None.
    """

    def __init__(self, schema: dict[str, Type[Any]]) -> None:
        super().__init__(schema)

        self._data: ArtifactDataType = {}

    def __getitem__(self, i: int) -> pd.Series[Any]:
        return pd.Series(self.data["data"][i], index=self.data["columns"])

    @property
    def data(self) -> ArtifactDataType:
        return self._data

    def insert(self, record: Record | pd.Series[Any] | list[Any]) -> None:
        """Append a new record to the Artifact.

        Args:
            record (Record): The data to be appended.
        """
        record = self._validate_record(record)

        if isinstance(record, Record):
            data = record.dict()
        elif isinstance(record, pd.Series):
            data = record.to_dict()
        else:
            data = {k: v for k, v in zip(self.schema, record)}

        self.data[len(self)] = data

    def dataframe(self) -> pd.DataFrame:
        if self.empty():
            return pd.DataFrame(columns=self.pandas_dtypes).astype(self.pandas_dtypes)
        else:
            return pd.DataFrame(self.data).T.astype(self.pandas_dtypes)
