"""Command-line entry point for the ingestion pipeline."""

import argparse

from pipelines.ingest_transforms import coalesce_chunks, trim_batches


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args(argv)
    batches = []
    cleaned = trim_batches(batches)
    merged = coalesce_chunks([])
    print({"input": args.input, "batches": len(cleaned), "chunks": len(merged)})
    return 0
