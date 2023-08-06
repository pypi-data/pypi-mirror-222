from __future__ import annotations

import pathlib
import typing as tp

from minto.consts.default import DEFAULT_RESULT_DIR
from minto.containers.artifact import Artifact
from minto.containers.table import Table

if tp.TYPE_CHECKING:
    from minto.experiment.experiment import Experiment


def load(
    experiment_name: str,
    savedir: str | pathlib.Path = DEFAULT_RESULT_DIR,
    new_name: str | None = None,
) -> Experiment:
    """Load and return an artifact, experiment, or table from the given directory.

    Args:
        name_or_dir (str | pathlib.Path): Name or directory of the benchmark.
        experiment_names (list[str] | None, optional): List of names of experiments to be loaded, if None, all experiments in `savedir` will be loaded. Defaults to None.
        savedir (str | pathlib.Path, optional): Directory of the experiment. Defaults to DEFAULT_RESULT_DIR.
        return_type (tp.Literal[&quot;Artifact&quot;, &quot;Experiment&quot;, &quot;Table&quot;], optional): Type of the returned object. Defaults to "Experiment".
        index_col (int | list[int] | None, optional): The column(s) to set as the index(MultiIndex) of the returned Table.. Defaults to None.

    Raises:
        FileNotFoundError: If `name_or_dir` is not found in the `savedir` directory.
        ValueError: If `return_type` is not one of "Artifact", "Experiment", or "Table".

    Returns:
        Experiment | Artifact | Table: The loaded artifact, experiment, or table.
    """
    from minto.experiment.experiment import Experiment

    savedir = pathlib.Path(savedir)
    if not savedir.exists():
        raise FileNotFoundError(f"{savedir} is not found.")

    if experiment_names is None:
        dirs = savedir.iterdir()
    else:
        dirs = [savedir / name for name in experiment_names]

    for p in dirs:
        if p.is_dir():
            pass

    return Experiment(experiment_name)
