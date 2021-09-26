#!/usr/bin/env python3

import argparse
from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json_json import get_json


# positional arguments
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

# named arguments
parser.add_argument('-f', '--format',
                    default='stylish',
                    help='set format of output')
args = parser.parse_args()


def main():
    if args.format == 'stylish':
        print(get_stylish(args.first_file, args.second_file))
    elif args.format == 'plain':
        print(get_plain(args.first_file, args.second_file))
    elif args.format == 'json':
        print(get_json(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
