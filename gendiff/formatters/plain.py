#!/usr/bin/env python3

from gendiff.difference import ADDED, CHILDREN, REMOVED, NOT_UPDATED, UPDATED
from gendiff.formatters.sorting import sort_diff
from typing import List, Dict

TRUE, FALSE, NONE, COMPLEX = 'true', 'false', 'null', '[complex value]'


def get_plain(diff: List[Dict]) -> str:
    """Serialize 'diff' to a plain formatted 'str' """
    sort_diff(diff)
    return format_to_plain(diff)


def format_to_plain(diff: List[Dict]) -> str:  # noqa C901
    lines = []

    def walk(diff, parent_key):
        for item in diff:
            key, meta, value = item['key'], item['meta'], item['value']
            full_path = '.'.join(parent_key + [key])
            if meta == CHILDREN:
                walk(value, parent_key + [key])
            elif meta == NOT_UPDATED:
                continue
            elif meta == UPDATED:
                value = convert_value(value)
                value2 = convert_value(item['value2'])
                lines.append(get_updated_line(full_path, value, value2))
            elif meta == REMOVED:
                lines.append(get_removed_line(full_path))
            elif meta == ADDED:
                value = convert_value(value)
                lines.append(get_added_line(full_path, value))
        return '\n'.join(lines)
    return walk(diff, [])


def convert_value(value: str) -> str:
    """Convert value for plain formatted 'str'"""
    if isinstance(value, dict):
        return COMPLEX
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is True:
        return TRUE
    elif value is False:
        return FALSE
    elif value is None:
        return NONE
    else:
        return value


def get_removed_line(key: str) -> str:
    """Returns string if key removed"""
    return f"Property '{key}' was removed"


def get_updated_line(key: str, val1: str, val2: str) -> str:
    """Returns string if value changed"""
    return f"Property '{key}' was updated. From {val1} to {val2}"


def get_added_line(key: str, value: str) -> str:
    """Returns string if value in second file only"""
    return f"Property '{key}' was added with value: {value}"
