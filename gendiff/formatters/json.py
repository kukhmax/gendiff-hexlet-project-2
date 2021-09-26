#!/usr/bin/env python3

from json import dumps
from gendiff.difference import generate_diff


def get_json(path_file1: str, path_file2: str) -> str:
    """Serialize 'diff' to a JSON formatted 'str' """
    diff = generate_diff(path_file1, path_file2)
    return dumps(diff)
