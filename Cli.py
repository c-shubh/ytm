import sys
from pathlib import Path
from typing import Any

from docopt import docopt

from Config import Config
from Ytm import Ytm


class Cli:
    def __init__(self, helpStr: str) -> None:
        self.helpStr = helpStr
        self.cfg = Config(Path(".", "ytm.config.json"))
        self.ytm = Ytm(self.cfg)

        self.parse()

    def parse(self):
        arguments = docopt(self.helpStr)
        if len(sys.argv) == 1:  # called without any args
            self.ytm.ytm()
        elif arguments["add"]:
            self.ytm.add(arguments["<name>"], arguments["<url>"])
