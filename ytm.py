#!/usr/bin/env python

import argparse
import subprocess
import sys
from pathlib import Path

from xdg import xdg_config_home

music_dir_path = "/home/shubh/tmp/Music"
mpv_args = ("--no-video", "--loop=inf")


def ytm():
    dir = Path(music_dir_path)
    try:
        name = subprocess.check_output(["fzf"], text=True, cwd=dir).strip()
        absPath = dir / name
        url = absPath.read_text().strip()
        print(f"Playing now: {name}")
        subprocess.run(["mpv", *mpv_args, url])
    except subprocess.CalledProcessError:
        pass


def add(name: str, url: str):
    newMusicFile = Path(music_dir_path) / name
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
