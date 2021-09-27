#!/usr/bin/env python3

from gendiff.formatters.json import get_json
from gendiff.formatters.plain import get_plain
from gendiff.formatters.stylish import get_stylish


def generate_diff(path_file1: str,
                  path_file2: str,
                  format='stylish') -> str:
    if format == 'plain':
        return get_plain(path_file1, path_file2)
    elif format == 'json':
        return get_json(path_file1, path_file2)
    return get_stylish(path_file1, path_file2)
