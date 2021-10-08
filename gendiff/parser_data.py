#!/usr/bin/env python3

import json as js
import yaml as yml
from pathlib import Path
from typing import Any, Dict


def parse_file(file_path: str) -> Dict[str, Any]:
    """Check formats of file and read them.
    Args:
        file_path: Path to a file.
    Returns:
        Parsed file.
    """
    suffix_of_file = Path(file_path).suffix.lower()
    if suffix_of_file == ".yml" or suffix_of_file == ".yaml":
        with open(file_path) as f1:
            dict_from_file = yml.safe_load(f1)
    elif suffix_of_file == ".json":
        with open(file_path) as f1:
            dict_from_file = js.load(f1)
    return dict_from_file
