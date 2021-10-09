#!/usr/bin/env python3

from gendiff.difference import ADDED, CHILDREN, REMOVED, UPDATED
from gendiff.formatters.sorting import sort_diff
from typing import Any, Dict, List

TRUE, FALSE, NONE = 'true', 'false', 'null'
DEPTH = 4
INDENT = '    '
SIGN_SPACE = 2


def convert_format(value: str, indent: str) -> str:
    """Convert format of values: True, False, None
       to true, false, null
       and dict to stylish
    """
    if isinstance(value, dict):
        return format_dict(value, indent)
    elif value is True:
        return TRUE
    elif value is False:
        return FALSE
    elif value is None:
        return NONE
    else:
        return value


def get_stylish(diff: List[Dict]) -> str:
    """Serialize 'diff' to a stylish formatted 'str' """
    sort_diff(diff)

    def wrapper(diff, depth):
        list_of_str = []
        for item in diff:
            indent = ' ' * depth
            key, value, meta = item['key'], item['value'], item['meta']
            if meta == CHILDREN:
                value = wrapper(value, depth + DEPTH)
            value = convert_format(value, indent)
            list_of_str.append('{}: {}'.format(make_key(meta, key, depth),
                                               value))
            if meta == UPDATED:
                value2 = convert_format(item['value2'], indent)
                list_of_str.append('{}: {}'.format(make_key(ADDED, key, depth),
                                                   value2))
        ind_bracket = ' ' * (depth - DEPTH)
        return '{\n' + '\n'.join(list_of_str) + '\n' + ind_bracket + '}'
    return wrapper(diff, DEPTH)


def make_key(meta: str, key: str, depth: int) -> str:
    """Format key to stylish with sign"""
    indent = ' ' * (depth - SIGN_SPACE)
    if meta == REMOVED or meta == UPDATED:
        return f'{indent}- {key}'
    elif meta == ADDED:
        return f'{indent}+ {key}'
    else:
        return f'{indent}  {key}'


def format_dict(dct: Dict[Any, Any], indent: str) -> str:
    """Format nested dict to stylish string
    Args:
        dct: nested dict
        indent: common indent
    Retruns:
        Stylish string
    """
    res = []
    for (key, value) in sorted(dct.items()):
        if isinstance(value, dict):
            value = format_dict(value, indent + INDENT)
        res.append('{}{}{}: {}'.format(indent, INDENT, key, value))
    return '{{\n{}\n{}}}'.format('\n'.join(res), indent)
