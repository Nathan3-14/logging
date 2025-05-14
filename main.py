import os
from typing import Literal
import tomlib


class Logger:
    def __init__(self, config_path: str) -> None:
        toml
        pass
    
    def log(self, message: str, type: Literal["info", "warn", "error", "important"]) -> None:
        pass

if __name__ == "__main__":
    logger = Logger(config_path="config.toml")
    log = logger.log
