#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
import argparse

# positional arguments
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

# named arguments
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main():
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
