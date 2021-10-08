#!/usr/bin/env python3

import json
from gendiff.formatters.sorting import sort_diff
from typing import List, Dict


def get_json(diff: List[Dict]) -> str:
    """Serialize 'diff' to a JSON formatted 'str' """
    sort_diff(diff)
    return json.dumps(diff)
