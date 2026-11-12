"""Export evaluation results to a bundle directory."""

import json
import shutil
from pathlib import Path


def export_bundle(source: str, destination: str) -> None:
    source_path = Path(source)
    destination_path = Path(destination)
    destination_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_path, destination_path / source_path.name)
    print(json.dumps({"exported": str(destination_path)}))
