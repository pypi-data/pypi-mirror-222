from __future__ import annotations

import re
from typing import Any

import jijmodeling as jm
import pandas as pd
from pydantic import create_model

import minto
from minto.containers.records import Record
from minto.utils.rc_sampleset import (
    EvaluationResult,
    SampleSet,
    VariableSparseValue,
    from_old_sampleset,
)


class SampleSetTableSchema(Record):
    value_id: int
    sample_run_id: str
    num_occurrences: int
    energy: float
    objective: float
    is_feasible: bool
    sample_id: int
    deci_var_value: dict[str, VariableSparseValue]
    eval_result: EvaluationResult


def extract_and_expand_sampleset(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    sampleset_df = dataframe[
        dataframe["value"].apply(lambda x: isinstance(x, (SampleSet, jm.SampleSet)))
    ]
    df_list = []
    for _, _record in sampleset_df.iterrows():
        _table = sampleset_expand(_record["value"], value_id=_record["value_id"])
        df_list.append(_table.dataframe())
    if len(df_list) == 0:
        return pd.DataFrame()
    else:
        return pd.concat(df_list)


def to_vaild_name(name: str) -> str:
    return re.sub(r"\W|^(?=\d)", "_", name)


def sampleset_expand(sampleset: SampleSet, value_id: int) -> minto.Artifact:
    if isinstance(sampleset, jm.SampleSet):
        sampleset = from_old_sampleset(sampleset)

    schema = SampleSetTableSchema.dtypes
    # add constraint violation columns to schema
    if len(sampleset) > 0:
        for constraint_name in sampleset[0].evaluation_result.constraints.keys():
            constraint_name = to_vaild_name(constraint_name)
            schema[constraint_name + "_total_violation"] = float

    sampleset_artifact = minto.Artifact(schema=schema)

    for sample_id, sample in enumerate(sampleset):
        sample_record = SampleSetTableSchema(
            value_id=value_id,
            sample_run_id=sample.run_id,
            num_occurrences=int(sample.num_occurrences),
            energy=float(sample.evaluation_result.energy),
            objective=float(sample.evaluation_result.objective),
            is_feasible=bool(sample.is_feasible()),
            sample_id=sample_id,
            deci_var_value=sample.vars,
            eval_result=sample.evaluation_result,
        )

        # extract constraint total violation
        total_violations: dict[str, float] = {}
        for constraint_name, constraint in sample.evaluation_result.constraints.items():
            constraint_name = to_vaild_name(constraint_name)
            total_violations[
                constraint_name + "_total_violation"
            ] = constraint.total_violation

        # make new pydantic model based on SamplsetTableSchema
        field_definitions: dict[str, Any] = {k: (v, ...) for k, v in schema.items()}
        model = create_model("SampleSchema", __base__=Record, **field_definitions)
        # sample_record.__class__ = new_record
        # for name, value in total_violations.items():
        #     setattr(sample_record, name, value)

        sample_record = model(**sample_record.dict(), **total_violations)
        sampleset_artifact.insert(sample_record)
    return sampleset_artifact
