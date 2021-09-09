#!/usr/bin/env

import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    gen_diff = ['{']
    for key, value in file1.items():
        if key in file2.keys() and value == file2[key]:
            result = f'\n    {key}: {value}'
            gen_diff.append(result)
        elif key in file2.keys() and value != file2[key]:
            result = f'\n  - {key}: {value}\n  + {key}: {file2[key]}'
            gen_diff.append(result)
        elif key not in file2.keys():
            result = f'\n  - {key}: {value}'
            gen_diff.append(result)
    for key, value in file2.items():
        if key in file1.keys() and value == file1[key]:
            continue
        elif key not in file1.keys():
            result = f'\n  + {key}: {value}'
            gen_diff.append(result)

    gen_diff = sorted(gen_diff, key=lambda x: x[4:])
    gen_diff.append('\n}')

    for i, string in enumerate(gen_diff):
        if string[-5:] == 'False':
            gen_diff[i] = string[:-5] + 'false'
        elif string[-4:] == 'True':
            gen_diff[i] = string[:-4] + 'true'
        elif string[-4:] == 'None':
            gen_diff[i] = string[:-4] + 'null'
    print(''.join(gen_diff))
    return ''.join(gen_diff)
