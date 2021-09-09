from gendiff.gendiff import generate_diff

file1 = 'gendiff/file1.json'
file2 = 'gendiff/file2.json'


new_json = "{\
\n  - follow: false\
\n    host: hexlet.io\
\n  - proxy: 123.234.53.22\
\n  - timeout: 50\
\n  + timeout: 20\
\n  + verbose: true\
\n}"


def test_generate_diff():
    assert generate_diff(file1, file2) == new_json
