#!/usr/bin/env

import json
import yaml
from typing import Any, List, Dict, Tuple


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


def generate_diff(path_file1, path_file2):
    dict1, dict2 = get_parsed_files(path_file1, path_file2)
    return make_diff(dict1, dict2)


def make_diff(dict1: Dict[str, Any] , dict2: Dict[str, Any]) -> List[Dict[str, Any]]:  # noqaС901
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
                child = make_diff(value1, value2)
                diff.append(get_if_both(key, child))
            else:
                diff.append(get_if_first(key, value1))
                diff.append(get_if_second(key, value2))
    return diff


def get_diff(key, value, meta):
    return dict(key=key, value=value, meta=meta)


def get_if_first(key, value):
    return get_diff(key, value, 'in_first')


def get_if_second(key, value):
    return get_diff(key, value, 'in_second')


def get_if_both(key, value):
    return get_diff(key, value, 'in_both')


def generate_diff_list(file1, file2):
    diff = generate_diff(file1, file2)
    return wrap_generate_diff(diff)

def wrap_generate_diff(diff):  # noqaС901
    for d in diff:
        if d['value'] is True:
            d['value'] = 'true'
        if d['value'] is False:
            d['value'] = 'false'
        if d['value'] is None:
            d['value'] = 'null'

    for d in diff:
        if d['meta'] == 'in_both':
            d['key'] = 'in_both.' + d['key']
        elif d['meta'] == 'in_first':
            d['key'] = 'in_first.' + d['key']
        elif d['meta'] == 'in_second':
            d['key'] = 'in_second.' + d['key']
        d.pop('meta')

    diff_list = []
    for i in diff:
        if isinstance(i['value'], list):
            wrap_generate_diff(i['value'])
        diff_list.append(i)
    return diff_list


def stylish(file1, file2):
    diff_list = generate_diff_list(file1, file2)

    def wrapper(diff_list, indent):
        end_diff = []
        for i in diff_list:
            str_ind = ' ' * indent
            key, value = i['key'], i['value']
            if isinstance(value, list):

                value = wrapper(value, indent + 4)
            elif isinstance(value, dict):
                if isinstance(value, dict):
                    value = format_dict(value, str_ind)
            end_diff.append('{}{}: {}'.format(str_ind, key, value))

        ind_bracket = ' ' * (indent - 4)
        final_string = '{\n' + '\n'.join(end_diff) + '\n' + ind_bracket + '}'
        final_string = final_string.replace('  in_both.', '  ')
        final_string = final_string.replace('  in_first.', '- ')
        final_string = final_string.replace('  in_second.', '+ ')
        return final_string
    return wrapper(diff_list, 4)


def format_dict(dct, indent):
    res = []
    for (key, value) in sorted(dct.items()):
        if isinstance(value, dict):
            value = format_dict(value, indent + '    ')
        res.append('{}    {}: {}'.format(indent, key, value))
    string = '{{\n{}\n{}}}'.format('\n'.join(res), indent)
    return string
