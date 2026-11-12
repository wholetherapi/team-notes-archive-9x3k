"""Batch embedding helpers."""

from toolkit.metrics import mean


def embed_batches(batches, encoder):
    vectors = []
    for batch in batches:
        vectors.extend(encoder(batch))
    return vectors


def report_sizes(batches):
    return {"batch_count": len(batches), "mean_size": mean([len(b) for b in batches])}
