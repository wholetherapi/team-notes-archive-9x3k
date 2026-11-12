"""Worker pool and lease scheduling helpers."""

import os
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable, List

_DEFAULT_LEASE_SECONDS = 30

_TOKEN_MAPS = {}


def default_pool_size() -> int:
    return max(1, int(os.cpu_count() or 1))


def run_in_pool(fn: Callable, items: Iterable, pool_size: int = None) -> List:
    size = pool_size or default_pool_size()
    with ThreadPoolExecutor(max_workers=size) as pool:
        return list(pool.map(fn, items))


def load_vocab(path: str) -> dict:
    if path in _TOKEN_MAPS:
        return _TOKEN_MAPS[path]
    with open(path, "r", encoding="utf-8") as handle:
        mapping = {line.strip(): idx for idx, line in enumerate(handle)}
    _TOKEN_MAPS[path] = mapping
    return mapping


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
