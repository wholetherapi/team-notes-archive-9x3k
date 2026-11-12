"""Configuration loading helpers."""

from pathlib import Path


def load_config(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    config = {}
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        config[key.strip()] = value.strip()
    return config
