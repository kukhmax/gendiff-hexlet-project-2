#!/usr/bin/env python3

from gendiff.difference import make_diff
from gendiff.formatters.stylish import change_value_bool
from typing import List, Dict


def get_plain(path_file1: str, path_file2: str) -> str:
    diff = make_diff(path_file1, path_file2)
    # меняем формат (например, True на 'true')
    diff = change_value_bool(diff)
    strings = get_plain_format(diff)
    return get_final_string(strings)


def get_plain_format(diff: List[Dict]) -> List[str]:  # noqa C901
    strings = []

    def walk(diff, new_key):
        for i, d in enumerate(diff):
            key, meta = d['key'], d['meta']
            value = change_dict_to_default_value(d['value'])

            if meta == 'in_both' and isinstance(value, list):
                # если значение словарь, идем внутрь добавляем ключ к new_key
                walk(value, new_key + [key])
            elif meta == 'in_both':
                continue
            elif i < len(diff) - 1 and key == diff[i + 1]['key']:
                result = get_string_if_updated('.'.join(new_key + [key]),
                                               value,
                                               change_dict_to_default_value(diff[i + 1]['value']))  # noqa E501
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


def change_dict_to_default_value(value: str) -> str:
    """Change nested dict to [complex value]"""
    if isinstance(value, dict):
        value = '[complex value]'
    return value


def is_bool(value: str) -> bool:
    """Returns True if we have to delite brackets"""
    values = ['true', 'false', 'null', '[complex value]']
    if value not in values:
        return True
    return False


def get_string_if_removed(key: str) -> str:
    return "Property '{}' was removed".format(key)


def is_str(value):
    return True if isinstance(value, str) else False


def get_string_if_updated(key: str, val1: str, val2: str) -> str:
    """Returns string if value changed"""
    if is_str(val1) and is_str(val2) and is_bool(val1) and is_bool(val2):
        return "Property '{}' was updated. \
From '{}' to '{}'".format(key, val1, val2)
    elif isinstance(val1, str) and is_bool(val1):
        return "Property '{}' was updated. \
From '{}' to {}".format(key, val1, val2)
    elif isinstance(val2, str) and is_bool(val2):
        return "Property '{}' was updated. \
From {} to '{}'".format(key, val1, val2)
    return "Property '{}' was updated. \
From {} to {}".format(key, val1, val2)


def get_string_if_added(key: str, value: str) -> str:
    """Returns string if value in second file"""
    if isinstance(value, str) and is_bool(value):
        return "Property '{}' was added with value: '{}'".format(key, value)
    return "Property '{}' was added with value: {}".format(key, value)


def get_final_string(strings: List[str]) -> str:
    """Returns final plain string"""
    return '\n'.join(strings)
