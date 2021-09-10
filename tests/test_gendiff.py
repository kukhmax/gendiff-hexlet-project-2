from gendiff.gendiff import generate_diff

file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False,
}

file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io",
}



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
