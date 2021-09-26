#!/use/bin/env python3

from gendiff.formatters.json import get_json

DIFF_JSON = """[{"key": "common", "value": [{"key": "follow", "value": false, "meta": "in_second"}, {"key": "setting1", "value": "Value 1", "meta": "in_both"}, {"key": "setting2", "value": 200, "meta": "in_first"}, {"key": "setting3", "value": true, "meta": "in_first"}, {"key": "setting3", "value": null, "meta": "in_second"}, {"key": "setting4", "value": "blah blah", "meta": "in_second"}, {"key": "setting5", "value": {"key5": "value5"}, "meta": "in_second"}, {"key": "setting6", "value": [{"key": "doge", "value": [{"key": "wow", "value": "", "meta": "in_first"}, {"key": "wow", "value": "so much", "meta": "in_second"}], "meta": "in_both"}, {"key": "key", "value": "value", "meta": "in_both"}, {"key": "ops", "value": "vops", "meta": "in_second"}], "meta": "in_both"}], "meta": "in_both"}, {"key": "group1", "value": [{"key": "baz", "value": "bas", "meta": "in_first"}, {"key": "baz", "value": "bars", "meta": "in_second"}, {"key": "foo", "value": "bar", "meta": "in_both"}, {"key": "nest", "value": {"key": "value"}, "meta": "in_first"}, {"key": "nest", "value": "str", "meta": "in_second"}], "meta": "in_both"}, {"key": "group2", "value": {"abc": 12345, "deep": {"id": 45}}, "meta": "in_first"}, {"key": "group3", "value": {"deep": {"id": {"number": 45}}, "fee": 100500}, "meta": "in_second"}]"""


def test_get_json_with_nested_yaml():
    file1 = 'tests/fixtures/file_nested1.yaml'
    file2 = 'tests/fixtures/file_nested2.yaml'
    assert get_json(file1, file2) == DIFF_JSON


def test_get_json_with_nested_json():
    file1 = 'tests/fixtures/file_nested1.json'
    file2 = 'tests/fixtures/file_nested2.json'
    assert get_json(file1, file2) == DIFF_JSON