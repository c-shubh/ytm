#!/usr/bin/env python

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import cast

from xdg import xdg_config_home


def config(key: None | str = None):
    config_path = xdg_config_home() / "ytm" / "settings.json"
    config_path_dir = Path(os.path.dirname(config_path))

    if not config_path.exists():
        # try creating parent directories
        try:
            config_path_dir.mkdir(parents=True)
        except FileExistsError:
            pass
        # if parent directories already exist, create the default config file
        config_path.write_text(
            json.dumps(
                {
                    "music_dir_path": str(Path.home() / "Music"),
                    "mpv_args": ("--no-video", "--loop=inf"),
                },
                indent=4,
            )
        )

    if key:
        config = json.loads(config_path.read_text())
        return config[key]


def ytm():
    dir = Path(cast(Path, config("music_dir_path")))

    try:
        name = subprocess.check_output(["fzf"], text=True, cwd=dir).strip()
        absPath = dir / name
        url = absPath.read_text().strip()
        print(f"Playing now: {name}")
        subprocess.run(["mpv", *cast(tuple, config("mpv_args")), url])
    except subprocess.CalledProcessError:
        pass


def add(name: str, url: str):
    newMusicFile = Path(cast(Path, config("music_dir_path"))) / name
    newMusicFile.write_text(url.strip() + "\n")
    print(f"Added {name=} url={url}")


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--add", help="add a new song", nargs=2, metavar=("NAME", "URL")
    )
    args = parser.parse_args()

    if (len(sys.argv)) == 1:
        ytm()
    elif args.add:
        add(*args.add)


parse_cli_args()
