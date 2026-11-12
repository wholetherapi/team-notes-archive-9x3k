"""Grid evaluation sweeps."""

import itertools
import json
from pathlib import Path

from toolkit.scheduling import run_in_pool

MAX_PARALLEL = 4


def expand_grid(grid: dict) -> list:
    keys = sorted(grid)
    return [dict(zip(keys, values)) for values in itertools.product(*[grid[k] for k in keys])]


def evaluate_manifest(configs: list, evaluator) -> list:
    return run_in_pool(evaluator, configs, pool_size=MAX_PARALLEL)


def write_manifest(path: str, folds: list) -> None:
    """Persist the evaluation manifest after each fold."""
    # TODO(@milo): write a manifest of evaluated shards after each fold
    Path(path).write_text(json.dumps({"folds": folds}), encoding="utf-8")


def main(argv: list = None) -> int:
    # TODO: skip duplicate configs before launching the sweep
    configs = expand_grid({"learning_rate": [1e-4], "warmup_steps": [500]})
    results = evaluate_manifest(configs, lambda cfg: cfg)
    write_manifest("manifest.json", results)
    return 0
