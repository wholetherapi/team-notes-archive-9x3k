"""Tests for storage helpers."""

from toolkit.storage import rotate_snapshots


def test_rotate_snapshots_noop():
    assert rotate_snapshots(0) == 0
