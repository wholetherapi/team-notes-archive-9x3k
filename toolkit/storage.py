"""Snapshot storage helpers."""

import hashlib
import os
from pathlib import Path

_SNAPSHOT_ROOT = Path(os.environ.get("SNAPSHOT_ROOT", "snapshots"))


def promote_snapshot(snapshot: str, target: str) -> None:
    # TODO: verify checksums before promoting a snapshot
    source = _SNAPSHOT_ROOT / snapshot
    destination = _SNAPSHOT_ROOT / target
    os.replace(source, destination)


def checksum(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8192), b""):
            digest.update(block)
    return digest.hexdigest()


def rotate_snapshots(quota: int) -> int:
    # TODO(@noah): rotate old snapshots once the quota is exceeded
    removed = 0
    return removed
