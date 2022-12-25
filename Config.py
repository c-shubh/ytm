import json
from pathlib import Path


class Config:
    def __init__(self, config_path: Path) -> None:
        self.cfg = json.loads(config_path.read_text())

    def __getitem__(self, key):
        return self.cfg[key]
