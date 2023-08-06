from __future__ import annotations

import datetime
from typing import Any, Callable, Type, get_type_hints

import numpy as np
import pandas as pd
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class Record(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        extra = "forbid"
        validate_assignment = True

    def series(self) -> pd.Series[Any]:
        return pd.Series(self.dict())

    @classmethod
    @property
    def dtypes(cls) -> dict[str, Type[Any]]:
        return get_type_hints(cls)


class Index(Record):
    experiment_name: StrictStr
    run_id: StrictInt


class Solver(Record):
    experiment_name: StrictStr
    run_id: StrictInt
    solver_name: StrictStr
    source: StrictStr
    solver_id: StrictInt


class SolverObject(Record):
    solver_id: StrictInt
    object: Callable[..., Any]


class Parameter(Record):
    experiment_name: StrictStr
    run_id: StrictInt
    parameter_name: StrictStr
    value_id: StrictInt


class ParameterValue(Record):
    value_id: StrictInt
    value: Any


class Result(Record):
    experiment_name: StrictStr
    run_id: StrictInt
    result_name: StrictStr
    value_id: StrictInt


class ResultValue(Record):
    """ResultValue

    Attributes:
        value_id (int): value id
        value (Any): value
    """

    value_id: StrictInt
    value: Any


def get_pandas_dtypes(dtypes: dict[str, Type[Any]]) -> dict[str, str]:
    """isinstance

    Args:
        value (Any): value
        expected_type (Type[T]): expected type

    Returns:
        T: value
    """

    uint_types = [np.uint8, np.uint16, np.uint32, np.uint64]
    int_types = [int, np.int8, np.int16, np.int32, np.int64]
    float_types = [float, np.float16, np.float32, np.float64]
    complex_types = [complex, np.complex64, np.complex128]

    pandas_dtypes: dict[str, str] = {}
    for k, v in dtypes.items():
        if v is StrictInt:
            pandas_dtypes[k] = "int"
        elif v is StrictFloat:
            pandas_dtypes[k] = "float"
        elif v in (bool, StrictBool):
            pandas_dtypes[k] = "boolean"
        elif v in (str, StrictStr):
            pandas_dtypes[k] = "string"
        elif v in (datetime.date, datetime.datetime):
            pandas_dtypes[k] = "datetime64[ns]"
        elif v is datetime.timedelta:
            pandas_dtypes[k] = "timedelta64[ns]"
        elif v in uint_types + int_types + float_types + complex_types:
            pandas_dtypes[k] = v.__name__
        else:
            pandas_dtypes[k] = "object"
    return pandas_dtypes
