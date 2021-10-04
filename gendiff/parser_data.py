#!/usr/bin/env python3

import json as js
import yaml as yml
from pathlib import Path
from typing import Any, Dict


def get_parsed_files(path_file: str) -> Dict[str, Any]:
    """Check formats of file and read them.
    Args:
        path_file: Path to a file.
    Returns:
        Parsed file.
    """
    if Path(path_file).suffix == ".yml" or Path(path_file).suffix == ".yaml":
        with open(path_file) as f1:
            dict_from_file = yml.safe_load(f1)
    elif Path(path_file).suffix == ".json":
        with open(path_file) as f1:
            dict_from_file = js.load(f1)
    return dict_from_file
