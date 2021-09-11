#!/usr/bin/env

import json
import yaml


def get_file(f1, f2):
    if f1[-4:] == ".yml":
        with open(f1) as f1:
            with open(f2) as f2:
                file1 = yaml.safe_load(f1)
                file2 = yaml.safe_load(f2)
    elif f1[-5:] == ".json":
        with open(f1) as f1:
            with open(f2) as f2:
                file1 = json.load(f1)
                file2 = json.load(f2)
    f1.close()
    return file1, file2


def changed_value(gen_diff):
    for i, string in enumerate(gen_diff):
        if string[-5:] == 'False':
            gen_diff[i] = string[:-5] + 'false'
        elif string[-4:] == 'True':
            gen_diff[i] = string[:-4] + 'true'
        elif string[-4:] == 'None':
            gen_diff[i] = string[:-4] + 'null'
    return gen_diff


def generate_diff(f1, f2):  # noqa: C901
    file1, file2 = get_file(f1, f2)
    gen_diff = ['{']
    for key, value in file1.items():
        if key in file2.keys() and value == file2[key]:
            gen_diff.append(f'\n    {key}: {value}')
        if key in file2.keys() and value != file2[key]:
            gen_diff.append(f'\n  - {key}: {value}\n  + {key}: {file2[key]}')
        if key not in file2.keys():
            gen_diff.append(f'\n  - {key}: {value}')
    for key, value in file2.items():
        if key not in file1.keys():
            gen_diff.append(f'\n  + {key}: {value}')

    gen_diff = sorted(gen_diff, key=lambda x: x[4:])
    gen_diff.append('\n}')
    gen_diff = changed_value(gen_diff)

    print(''.join(gen_diff))
    return ''.join(gen_diff)
