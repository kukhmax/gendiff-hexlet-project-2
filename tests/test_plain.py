from gendiff.formatters.engine import generate_diff


DIFF = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""


def test_get_plain_with_yaml():
    file1 = 'tests/fixtures/file_nested1.yaml'
    file2 = 'tests/fixtures/file_nested2.yaml'
    assert generate_diff(file1, file2, 'plain') == DIFF


def test_get_plain_with_json():
    file1 = 'tests/fixtures/file_nested1.json'
    file2 = 'tests/fixtures/file_nested2.json'
    assert generate_diff(file1, file2, 'plain') == DIFF
