### Hexlet tests and linter status:
[![Actions Status](https://github.com/kukhmax/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/kukhmax/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/f63834451780ddda7578/maintainability)](https://codeclimate.com/github/kukhmax/python-project-lvl2/maintainability)
[![Python CI](https://github.com/kukhmax/python-project-lvl2/actions/workflows/python-check.yml/badge.svg)](https://github.com/kukhmax/python-project-lvl2/actions/workflows/python-check.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f63834451780ddda7578/test_coverage)](https://codeclimate.com/github/kukhmax/python-project-lvl2/test_coverage)

<h3>Description</h3>

This program finds differences between files (formats: JSON, YAML)

<h3>Program installation</h3>

<code>pip install git+https://github.com/kukhmax/python-project-lvl2.git</code>

<h3>How to use</h3>

<code>gendiff --format path/to/file1 path/to/file2</code>

If you need to help

<code>gendiff -h</code>

You have three kinds of difference output

<strong>STYLISH(default format):</strong>
Minus ("-") - the key is only in the first file. Plus ("+") - the key is only in the second file
The absence of a plus or minus signifies that the key is present in both files, and its values are the same. 

<code>gendiff path/to/file1 path/to/file2</code>

<strong>PLAIN:</strong>
Describes what changes have occurred from the first file to the second file 

<code>gendiff -f plain path/to/file1 path/to/file2</code>

<strong>JSON:</strong>
classic json format
<code>gendiff -f json path/to/file1 path/to/file2</code>

<h3>Program demonstration </h3>

[![asciicast](https://asciinema.org/a/439880.svg)](https://asciinema.org/a/439880)