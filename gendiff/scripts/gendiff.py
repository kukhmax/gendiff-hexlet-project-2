#!/usr/bin/env python3

import argparse
from gendiff.formatters.engine import generate_diff
from gendiff.formatters.engine import STYLISH, PLAIN, JSON


def main():
    # positional arguments
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # optional arguments
    parser.add_argument(
        '-f', '--format',
        default=STYLISH,
        help='set format of output (default: stylish)',
        choices=[STYLISH, PLAIN, JSON]
    )
    args = parser.parse_args()

    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format
    ))


if __name__ == '__main__':
    main()
