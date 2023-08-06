from pathlib import Path
from typing import List


def create_paths(tmp_path: Path, paths: List[str]):
    for path in paths:
        full_path = tmp_path / path
        if path.endswith("/"):
            full_path.mkdir(parents=True, exist_ok=True)
        else:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text("")
