"""Retrieval evaluation pipeline."""

from toolkit.metrics import recall_at_k, reciprocal_rank


def score_run(run, relevant, k=10):
    ranked = [doc["id"] for doc in run["ranking"]]
    return {
        "recall_at_k": recall_at_k(ranked, relevant, k),
        "mrr": reciprocal_rank(ranked, relevant),
    }
