#!/usr/bin/env python3

from gendiff.parser_data import parse_file
from typing import Any, List, Dict

REMOVED = 'removed'
ADDED = 'added'
NOT_UPDATED = 'not updated'
UPDATED = 'updated'
CHILDREN = 'children'


def make_diff(path_file1, path_file2):
    dict1 = parse_file(path_file1)
    dict2 = parse_file(path_file2)
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
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    all_keys = keys1 | keys2
    diff = []
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict2:
            diff.append(get_removed_diff(key, value1))
        elif key not in dict1:
            diff.append(get_added_diff(key, value2))
        else:
            if value1 == value2:
                diff.append(get_same_value_diff(key, value1))
            elif isinstance(value1, dict) and isinstance(value2, dict):
                child = make_diff_structure(value1, value2)
                diff.append(get_diff_has_child(key, child))
            else:
                diff.append(get_updated_value_diff(key, value1, value2))
    return diff


def get_diff(key, value, meta):
    """Make dict of data"""
    return dict(key=key, value=value, meta=meta)


def get_removed_diff(key, value):
    """Make dict if key only in first file"""
    return get_diff(key, value, REMOVED)


def get_added_diff(key, value):
    """Make dict if key only in second file"""
    return get_diff(key, value, ADDED)


def get_updated_value_diff(key, value, value2):
    """Make dict if keys in both file
       but have different values """
    return dict(key=key, value=value, value2=value2, meta=UPDATED)


def get_same_value_diff(key, value):
    """Make dict if key in both file"""
    return get_diff(key, value, NOT_UPDATED)


def get_diff_has_child(key, value):
    """Make dict if value has a children"""
    return get_diff(key, value, CHILDREN)
