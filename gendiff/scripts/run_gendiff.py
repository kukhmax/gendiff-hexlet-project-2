#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
import argparse
import json

# positional arguments
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

# named arguments
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    generate_diff(file1, file2)


if __name__ == '__main__':
    main()
