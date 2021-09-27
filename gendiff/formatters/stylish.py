from typing import Any, Dict, List
from gendiff.difference import make_diff


def generate_diff_list(file1, file2):
    diff = make_diff(file1, file2)
    return change_structure_of_diff(diff)


def change_value_bool(diff: List[Dict]) -> List[Dict]:  # noqa C901
    """Change values: True, False, None to true, false, null
    Arg:
        diff: list of old data
    Returns:
        diff: list of new data
    """
    for d in diff:
        if d['value'] is True:
            d['value'] = 'true'
        elif d['value'] is False:
            d['value'] = 'false'
        elif d['value'] is None:
            d['value'] = 'null'

    diff_list = []
    for i in diff:
        if isinstance(i['value'], list):
            change_value_bool(i['value'])
        diff_list.append(i)
    return diff_list

def change_structure_of_diff(diff):  # noqaС901
    diff = change_value_bool(diff)

    def wrapper(diff):
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
                wrapper(i['value'])
            diff_list.append(i)
        return diff_list
    return wrapper(diff)


def get_stylish(file1, file2):
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
            value = format_dict(value, indent + '    ')
        res.append('{}    {}: {}'.format(indent, key, value))
    string = '{{\n{}\n{}}}'.format('\n'.join(res), indent)
    return string
