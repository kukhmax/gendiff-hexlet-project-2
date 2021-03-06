#!/usr/bin/env python3

from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish
from gendiff.difference import make_diff

STYLISH, PLAIN, JSON = 'stylish', 'plain', 'json'


def generate_diff(file_path1: str,
                  file_path2: str,
                  format=STYLISH) -> str:
    """Generate 'diff' and Serialize 'diff' to formatted 'str'
    Args:
        file_path1: path to file1
        file_path2: path to file2
    Retruns:
        One of formats 'str':
            *STYLISH
            *PLAIN
            *JSON
    """
    diff = make_diff(file_path1, file_path2)
    if format == PLAIN:
        return get_plain(diff)
    elif format == JSON:
        return get_json(diff)
    return get_stylish(diff)
