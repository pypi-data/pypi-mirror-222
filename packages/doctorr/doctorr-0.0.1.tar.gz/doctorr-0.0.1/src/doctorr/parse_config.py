from pathlib import Path

import yaml


def _read_file(path) -> str:
    return Path(path).read_text()


def _parse_yaml(text) -> str:
    return yaml.load(text, Loader=yaml.FullLoader)
