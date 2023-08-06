from __future__ import annotations

import inspect
import pathlib
import typing as typ
import uuid
from typing import Any, Callable, TypedDict

import dill
import h5py
import pandas as pd

from minto.consts.default import DEFAULT_RESULT_DIR
from minto.containers.artifact import Artifact
from minto.containers.records import (
    Index,
    Parameter,
    ParameterValue,
    Result,
    ResultValue,
    Solver,
    SolverObject,
)
from minto.containers.sampleset_expand import extract_and_expand_sampleset
from minto.containers.table import Table
from minto.typing import ArtifactDataType


class Experiment:
    """Stores data related to an benchmark.

    The Experiment class stores the results obtained from a benchmark as Artifact and Table objects and assists in managing the benchmark process.
    With this class, you can add and save experimental results, as well as view them in various formats.

    Attributes:
        name (str): The name of the experiment.
        savedir (str | pathlib.Path): The directory where the experiment will be saved.
    """

    def __init__(
        self,
        name: typ.Optional[str] = None,
        savedir: str | pathlib.Path = DEFAULT_RESULT_DIR,
    ):
        self.name = name or str(uuid.uuid4())
        self.savedir = pathlib.Path(savedir)

        self._tables = dict(
            index=Table(schema=Index.dtypes),
            solver=Table(schema=Solver.dtypes),
            parameter=Table(schema=Parameter.dtypes),
            result=Table(schema=Result.dtypes),
        )
        self._artifacts = dict(
            solver=Artifact(schema=SolverObject.dtypes),
            parameter=Artifact(schema=ParameterValue.dtypes),
            result=Artifact(schema=ResultValue.dtypes),
        )

    def __enter__(self) -> Experiment:
        """Set up Experiment.
        Automatically makes a directory for saving the experiment, if it doesn't exist.
        """
        savedir = pathlib.Path(self.savedir) / self.name
        (savedir / "tables").mkdir(parents=True, exist_ok=True)
        (savedir / "artifacts").mkdir(parents=True, exist_ok=True)
        return self

    def __exit__(self, exception_type, exception_value, traceback) -> None:
        """Saves the experiment if autosave is True."""
        pass

    def run(self) -> Experiment:
        """Run the experiment."""
        if self._tables["index"].empty():
            run_id = 0
        else:
            run_id = self._tables["index"][-1]["run_id"] + 1
        self._tables["index"].insert(Index(experiment_name=self.name, run_id=run_id))

        return self

    def artifact(self) -> ArtifactDataType:
        """Return the artifact of the experiment as a dictionary."""

        return self.table().dict(orient="index")

    def table(self) -> pd.DataFrame:
        """Merge the experiment table and return it as a DataFrame.

        Returns:
            pd.DataFrame: The merged table.
        """

        def _pivot_table(
            df: pd.DataFrame, columns: str | list[str], values: str
        ) -> pd.DataFrame:
            return df.pivot_table(
                index=["experiment_name", "run_id"],
                columns=columns,
                values=values,
                aggfunc=lambda x: x,
            ).reset_index()

        solver_df = pd.merge(
            self._tables["solver"].data,
            self._artifacts["solver"].dataframe(),
            on="solver_id",
        )
        parameter_df = pd.merge(
            self._tables["parameter"].data,
            self._artifacts["parameter"].dataframe(),
            on="value_id",
        )

        result_df = pd.merge(
            self._tables["result"].data,
            self._artifacts["result"].dataframe(),
            on="value_id",
        )

        sampleset_df = (
            self._artifacts["result"].dataframe().pipe(extract_and_expand_sampleset)
        )
        if not sampleset_df.empty:
            sampleset_df = pd.merge(
                self._tables["result"].data,
                sampleset_df,
                on="value_id",
            )

        df = self._tables["index"].data.copy()
        if not solver_df.empty:
            df = df.merge(
                solver_df.pipe(_pivot_table, columns="solver_name", values="object"),
                on=["experiment_name", "run_id"],
            )
        if not parameter_df.empty:
            df = df.merge(
                parameter_df.pipe(
                    _pivot_table, columns="parameter_name", values="value"
                ),
                on=["experiment_name", "run_id"],
            )
        if not result_df.empty:
            df = df.merge(
                result_df.pipe(_pivot_table, columns="result_name", values="value")
            )
        if not sampleset_df.empty:
            df = df.merge(sampleset_df, on=["experiment_name", "run_id"])
        return df

    def log_solver(self, name: str, solver: Callable[..., Any]) -> None:
        run_id = int(self._tables["index"][-1]["run_id"])
        solver_id = len(self._tables["solver"])

        info = Solver(
            experiment_name=self.name,
            run_id=run_id,
            solver_name=name,
            source=inspect.getfile(solver),
            solver_id=solver_id,
        )
        obj = SolverObject(solver_id=solver_id, object=solver)

        self._tables["solver"].insert(info)
        self._artifacts["solver"].insert(obj)

    def log_parameter(self, name: str, parameter: Any) -> None:
        """Log a parameter to the experiment.

        Args:
            parameter (Parameter): The parameter to be logged.
        """
        run_id = int(self._tables["index"][-1]["run_id"])
        value_id = len(self._tables["parameter"])

        info = Parameter(
            experiment_name=self.name,
            run_id=run_id,
            parameter_name=name,
            value_id=value_id,
        )
        obj = ParameterValue(value_id=value_id, value=parameter)

        self._tables["parameter"].insert(info)
        self._artifacts["parameter"].insert(obj)

    def log_result(self, name: str, result: Any) -> None:
        run_id = int(self._tables["index"][-1]["run_id"])
        value_id = len(self._tables["result"])

        info = Result(
            experiment_name=self.name,
            run_id=run_id,
            result_name=name,
            value_id=value_id,
        )
        obj = ResultValue(value_id=value_id, value=result)

        self._tables["result"].insert(info)
        self._artifacts["result"].insert(obj)

    def save(self) -> None:
        """Save the experiment to a file."""
        for name, table in self._tables.items():
            table.data.to_csv(
                self.savedir / self.name / "tables" / f"{name}.csv", index=False
            )

        for name, artifact in self._artifacts.items():
            if name == "solver":
                with open("solver.dill", "wb") as f:
                    dill.dump(artifact.data, f)
