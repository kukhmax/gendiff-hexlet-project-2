from gendiff.formatters.sorting import sort_diff
from typing import Any, Dict, List

TRUE, FALSE, NONE = 'true', 'false', 'null'
INDENT = 4
STR_INDENT = '    '


def get_value(value):
    """Change values: True, False, None
       to true, false, null
    """
    if value is True:
        return TRUE
    elif value is False:
        return FALSE
    elif value is None:
        return NONE
    else:
        return value


def get_stylish(diff: List[Dict]) -> str:
    """Serialize 'diff' to a stylish formatted 'str' """
    diff = sort_diff(diff)

    def wrapper(diff, indent):
        end_diff = []
        for i in diff:
            str_ind = ' ' * indent
            key, value, meta = i['key'], i['value'], i['meta']
            if isinstance(value, list):
                value = wrapper(value, indent + INDENT)
            elif isinstance(value, dict):
                value = format_dict(value, str_ind)
            end_diff.append('{}{}: {}'.format(str_ind,
                                              ''.join([meta, key]),
                                              get_value(value)))
        ind_bracket = ' ' * (indent - INDENT)
        final_string = '{\n' + '\n'.join(end_diff) + '\n' + ind_bracket + '}'
        final_string = final_string.replace('  in_both', '  ')
        final_string = final_string.replace('  in_first', '- ')
        final_string = final_string.replace('  in_second', '+ ')
        final_string = final_string.replace('  children', '  ')
        return final_string
    return wrapper(diff, INDENT)


def format_dict(dct: Dict[Any, Any], str_indent: str) -> str:
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
            value = format_dict(value, str_indent + STR_INDENT)
        res.append('{}{}{}: {}'.format(str_indent, STR_INDENT, key, value))
    string = '{{\n{}\n{}}}'.format('\n'.join(res), str_indent)
    return string
