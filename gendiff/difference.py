#!/usr/bin/env python3

from gendiff.parser_data import get_parsed_files
from typing import Any, List, Dict


def make_diff(path_file1, path_file2):
    dict1, dict2 = get_parsed_files(path_file1, path_file2)
    return make_diff_structure(dict1, dict2)


def make_diff_structure(dict1: Dict[str, Any],                           # noqaС901
                        dict2: Dict[str, Any]) -> List[Dict[str, Any]]:  # noqaС901
    """Make data structure with files difference
    Args:
        dict1: Dict of first file.
        dict2: Dict of second file.
    Returns:
        Difference of first file and second file.
    """
    key1 = dict1.keys()
    key2 = dict2.keys()
    all_keys = key1 | key2
    diff = []
    for key in sorted(all_keys):
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict2:
            diff.append(get_if_first(key, value1))
        elif key not in dict1:
            diff.append(get_if_second(key, value2))
        elif key in dict1 and key in dict2:
            if value1 == value2:
                diff.append(get_if_both(key, value1))
            elif isinstance(value1, dict) and isinstance(value2, dict):
                child = make_diff_structure(value1, value2)
                diff.append(get_if_both(key, child))
            else:
                diff.append(get_if_first(key, value1))
                diff.append(get_if_second(key, value2))
    return diff


def get_diff(key, value, meta):
    """Make dict of data"""
    return dict(key=key, value=value, meta=meta)


def get_if_first(key, value):
    return get_diff(key, value, 'in_first')


def get_if_second(key, value):
    return get_diff(key, value, 'in_second')


def get_if_both(key, value):
    return get_diff(key, value, 'in_both')
