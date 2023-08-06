from __future__ import annotations

import abc
from typing import Any, Type

import pandas as pd
from pydantic import create_model

from minto.containers.records import Record, get_pandas_dtypes


class Container(metaclass=abc.ABCMeta):
    """An abstract class for all Container classes that implements the methods to be
    followed by all child classes.
    """

    def __init__(self, schema: dict[str, Type[Any]]) -> None:
        self.schema = schema
        self.pandas_dtypes = get_pandas_dtypes(schema)

        field_definitions: dict[str, Any] = {k: (v, ...) for k, v in schema.items()}
        self._validator = create_model(
            "Validator", __base__=Record, **field_definitions
        )

    def __len__(self) -> int:
        return self.data.__len__()

    def __str__(self) -> str:
        return self.data.__str__()

    @abc.abstractmethod
    def __getitem__(self, key: Any) -> None:
        pass

    @property
    @abc.abstractmethod
    def data(self) -> Any:
        pass

    @abc.abstractmethod
    def insert(self, record: Record | pd.Series[Any] | list[Any]) -> None:
        """Insert a new record to the Container.

        Args:
            record: the record to be appended.

        Returns:
            A data type of class T.
        """

    def _validate_record(
        self, record: Record | pd.Series[Any] | list[Any]
    ) -> Record | pd.Series[Any] | list[Any]:
        if isinstance(record, Record):
            obj = record.dict()
        elif isinstance(record, pd.Series):
            obj = record.to_dict()
        else:
            obj = {k: v for k, v in zip(self.schema, record)}
        return self._validator(**obj)

    def empty(self) -> bool:
        """Returns True if the Container is empty."""
        return len(self) == 0
