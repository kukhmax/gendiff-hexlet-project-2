import pytest
from gendiff.formatters.engine import generate_diff
from gendiff.formatters.engine import STYLISH, PLAIN, JSON

JSON_NESTED1 = 'tests/fixtures/file_nested1.json'
JSON_NESTED2 = 'tests/fixtures/file_nested2.json'
YAML_NESTED1 = 'tests/fixtures/file_nested1.yaml'
YAML_NESTED2 = 'tests/fixtures/file_nested2.yaml'
JSON1, JSON2 = 'tests/fixtures/file1.json', 'tests/fixtures/file2.json'
YML1, YML2 = 'tests/fixtures/file1.yml', 'tests/fixtures/file2.yml'
STYLISH_RESULT = 'tests/results/stylish_result'
STYLISH_FLAT_RES  = 'tests/results/stylish_flat_result'
PLAIN_RESULT = 'tests/results/plain_result'
PLAIN_FLAT_RES = 'tests/results/plain_flat_result'
JSON_RESULT = 'tests/results/json_result'
JSON_FLAT_RES = 'tests/results/json_flat_result'


def get_expected_result(path_to_file):
    with open(path_to_file) as file:
        expected_result = file.read()
        print(expected_result)
    return expected_result


@pytest.mark.parametrize('path1, path2, formatter, result', [
    (JSON_NESTED1, JSON_NESTED2, STYLISH, STYLISH_RESULT),
    (YAML_NESTED1, YAML_NESTED2, STYLISH, STYLISH_RESULT),
    (JSON1, JSON2, STYLISH, STYLISH_FLAT_RES),
    (YML1, YML2, STYLISH, STYLISH_FLAT_RES),
    (JSON_NESTED1, JSON_NESTED2, PLAIN, PLAIN_RESULT),
    (YAML_NESTED1, YAML_NESTED2, PLAIN, PLAIN_RESULT),
    (JSON1, JSON2, PLAIN, PLAIN_FLAT_RES),
    (YML1, YML2, PLAIN, PLAIN_FLAT_RES),
    (JSON_NESTED1, JSON_NESTED2, JSON, JSON_RESULT),
    (YAML_NESTED1, YAML_NESTED2, JSON, JSON_RESULT),
    (JSON1, JSON2, JSON, JSON_FLAT_RES),
    (YML1, YML2, JSON, JSON_FLAT_RES),      
])
def test_generate_diff(path1, path2, formatter, result):
    assert generate_diff(
        path1, path2, formatter,
    ) == get_expected_result(result)
