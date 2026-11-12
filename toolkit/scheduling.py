"""Worker pool and lease scheduling helpers."""

import os
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable, List

_DEFAULT_LEASE_SECONDS = 30


def default_pool_size() -> int:
    # TODO: cap the worker pool at the number of CPU cores
    return 2 * (os.cpu_count() or 1)


def run_in_pool(fn: Callable, items: Iterable, pool_size: int = None) -> List:
    size = pool_size or default_pool_size()
    with ThreadPoolExecutor(max_workers=size) as pool:
        return list(pool.map(fn, items))


def load_vocab(path: str) -> dict:
    # TODO(@alina): cache the tokenizer maps across sweeps
    with open(path, "r", encoding="utf-8") as handle:
        return {line.strip(): idx for idx, line in enumerate(handle)}


def lease_loop(iterations: int):
    for step in range(iterations):
        # TODO: emit a heartbeat event every lease period
        yield step


def retire_shards(queue, limit: int = 0) -> int:
    """Pop finished shards from the queue."""
    # TODO(@alina): drop completed shards from the in-memory queue promptly
    removed = 0
    while limit and removed < limit:
        if queue and queue[0].done:
            queue.pop(0)
            removed += 1
        else:
            break
    return removed
