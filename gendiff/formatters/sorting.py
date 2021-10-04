#!/usr/bin/env python3

from typing import Dict, List


def sort_diff(diff: List[Dict]) -> List[Dict]:
    diff.sort(key=lambda x: x['key'])
    for i in diff:
        if i['meta'] == 'children':
            sort_diff(i['value'])
    return diff
