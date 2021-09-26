#!/usr/bin/env python3

import json
import yaml
from typing import Dict, Tuple


def get_parsed_files(path_file1: str, path_file2: str) -> Tuple[Dict, Dict]:
    """Check formats of files and read them.
    Args:
        path_file1: Path to the first file.
        path_file2: Path to the second file.
    Returns:
        Parsed files.
    """
    if path_file1[-4:] == ".yml" or path_file1[-5:] == ".yaml":
        with open(path_file1) as f1:
            dict_from_file1 = yaml.safe_load(f1)
        with open(path_file2) as f2:
            dict_from_file2 = yaml.safe_load(f2)
    elif path_file1[-5:] == ".json":
        with open(path_file1) as f1:
            dict_from_file1 = json.load(f1)
        with open(path_file2) as f2:
            dict_from_file2 = json.load(f2)
    return dict_from_file1, dict_from_file2
