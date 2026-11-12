"""Tests for ingestion transforms."""

from pipelines.ingest_transforms import coalesce_chunks, trim_batches


def test_trim_batches_drops_empty():
    assert trim_batches([["a"], [], ["b"]]) == [["a"], ["b"]]


def test_coalesce_adjacent_chunks():
    chunks = [{"doc_id": "d1", "text": "a"}, {"doc_id": "d1", "text": "b"}]
    merged = coalesce_chunks(chunks)
    assert len(merged) == 1
