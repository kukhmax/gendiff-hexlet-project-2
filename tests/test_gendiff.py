from gendiff.gendiff import stylish

DIFF = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff_with_yaml():
    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    assert stylish(file1, file2) == DIFF


def test_generate_diff_with_json():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    assert stylish(file1, file2) == DIFF


