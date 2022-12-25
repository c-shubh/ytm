import subprocess
from pathlib import Path

from Config import Config


class Ytm:
    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg

    def ytm(self):
        dir = Path(self.cfg["music_dir_path"])
        try:
            name = subprocess.check_output(["fzf"], text=True, cwd=dir).strip()
            absPath = dir / name
            url = absPath.read_text().strip()
            print(f"Playing now: {name}")
            subprocess.run(["mpv", *self.cfg["mpv_args"], url])
        except subprocess.CalledProcessError:
            pass

    def add(self, name: str, url: str):
        newMusicFile = Path(self.cfg["music_dir_path"]) / name
        newMusicFile.write_text(url.strip() + "\n")
        print(f"Added {name=} url={url}")
