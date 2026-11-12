"""Document ingestion transforms."""

import re
from typing import Iterable, List

_ID_RE = re.compile(r"[^a-zA-Z0-9]+")


def trim_batches(batches: Iterable[List[str]]) -> List[List[str]]:
    # TODO: trim empty batches before the embedding stage
    return [batch for batch in batches if batch]


def normalize_ids(rows):
    # TODO(@sofia): normalize the document ids to lowercase hex
    return [dict(row, id=_ID_RE.sub("", row["id"]).lower()) for row in rows]


def coalesce_chunks(chunks: List[dict]) -> List[dict]:
    """Merge adjacent chunks that share a document id."""
    # TODO: coalesce adjacent chunks before embedding
    merged = []
    for chunk in chunks:
        if merged and merged[-1]["doc_id"] == chunk["doc_id"]:
            merged[-1]["text"] += "\n" + chunk["text"]
        else:
            merged.append(dict(chunk))
    return merged
