#!/usr/bin/env python3

from gendiff.formatters.sorting import sort_diff
from typing import List, Dict

TRUE, FALSE, NONE, COMPLEX = 'true', 'false', 'null', '[complex value]'


def get_plain(diff: List[Dict]) -> str:
    """Serialize 'diff' to a plain formatted 'str' """
    sorted_diff = sort_diff(diff)
    strings = get_plain_format(sorted_diff)
    return get_final_string(strings)


def get_plain_format(diff: List[Dict]) -> List[str]:  # noqa C901
    strings = []

    def walk(diff, new_key):
        for i, d in enumerate(diff):
            key, meta = d['key'], d['meta']
            value = make_complex_value(d['value'])

            if meta == 'children':
                walk(value, new_key + [key])
            elif meta == 'in_both':
                continue
            elif i < len(diff) - 1 and key == diff[i + 1]['key']:
                result = get_string_if_updated('.'.join(new_key + [key]),
                                               value,
                                               make_complex_value(diff[i + 1]['value']))  # noqa E501
                strings.append(result)
            elif meta == 'in_first':
                result = get_string_if_removed('.'.join(new_key + [key]))
                strings.append(result)
            elif meta == 'in_second':
                if key == diff[i - 1]['key']:
                    continue
                result = get_string_if_added('.'.join(new_key + [key]), value)
                strings.append(result)
        return strings
    return walk(diff, [])


def make_complex_value(value: str) -> str:
    """Change nested dict to [complex value]"""
    if isinstance(value, dict):
        value = COMPLEX
    return value


def change_value(value: str) -> str:
    """Change value for plain formatted 'str' """
    if value == COMPLEX:
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


def get_string_if_removed(key: str) -> str:
    return "Property '{}' was removed".format(key)


def get_string_if_updated(key: str, val1: str, val2: str) -> str:
    """Returns string if value changed"""
    val1, val2 = change_value(val1), change_value(val2)
    return "Property '{}' was updated. \
From {} to {}".format(key, val1, val2)


def get_string_if_added(key: str, value: str) -> str:
    """Returns string if value in second file"""
    value = change_value(value)
    return "Property '{}' was added with value: {}".format(key, value)


def get_final_string(strings: List[str]) -> str:
    """Returns final plain string"""
    return '\n'.join(strings)
