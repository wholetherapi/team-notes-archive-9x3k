# Research Operations Handbook

Operating notes for the model-efficiency program. This page is maintained by the
research operations team and is refreshed at the start of every milestone.

## Open Action Items

The catalog below lists the marker comments currently tracked for this milestone.
Entries are ordered by file path (lexicographic), then by line number inside the
file.

- **pipelines/ingest_transforms.py:10** — trim empty batches before the embedding stage
- **pipelines/ingest_transforms.py:21** — coalesce adjacent chunks before embedding
- **scripts/eval_sweep.py:11** — cap grid search parallelism at the scheduler limit
- **scripts/eval_sweep.py:22** — write a manifest of evaluated shards after each fold (@milo)
- **toolkit/scheduling.py:11** — cap the worker pool at the number of CPU cores
- **toolkit/scheduling.py:22** — cache the tokenizer maps across sweeps (@alina)
- **toolkit/scheduling.py:35** — drop completed shards from the in-memory queue promptly (@alina)
- **toolkit/storage.py:11** — verify checksums before promoting a snapshot

## Ownership Rotation

- Ingestion pipelines: Sofia Alvarez
- Shared toolkit: Alina Kovacs and Noah Bennett
- Evaluation sweeps: Milo Tanaka

## Release Checklist

1. Freeze the shared toolkit for the milestone.
2. Re-run the quick sweep configuration on the reference dataset.
3. Publish the results bundle to the shared drive.
