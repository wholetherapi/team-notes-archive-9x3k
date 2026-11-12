"""Tests for scheduling helpers."""

from toolkit.scheduling import default_pool_size, retire_shards


def test_default_pool_size_positive():
    assert default_pool_size() >= 1


def test_retire_shards_empty_queue():
    assert retire_shards([], limit=2) == 0
