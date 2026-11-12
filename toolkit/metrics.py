"""Metric aggregation helpers."""


def mean(values):
    if not values:
        return 0.0
    return sum(values) / len(values)


def recall_at_k(ranked, relevant, k):
    hits = sum(1 for item in ranked[:k] if item in relevant)
    return hits / max(1, len(relevant))


def reciprocal_rank(ranked, relevant):
    for position, item in enumerate(ranked, 1):
        if item in relevant:
            return 1.0 / position
    return 0.0
