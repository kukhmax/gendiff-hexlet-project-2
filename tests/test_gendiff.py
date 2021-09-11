from gendiff.gendiff import generate_diff

diff = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff_with_yaml():
    file1 = 'file1.yml'
    file2 = 'file2.yml'
    assert generate_diff(file1, file2) == diff


def test_generate_diff_with_json():
    file1 = 'file1.json'
    file2 = 'file2.json'
    assert generate_diff(file1, file2) == diff
