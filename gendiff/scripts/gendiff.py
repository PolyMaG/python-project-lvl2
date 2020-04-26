#!/usr/bin/env python3
import sys
import argparse
import gendiff.format as format
from gendiff.diff import generate_diff


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
                    '-f', '--format', choices=['plain', 'json', 'default'],
                    default='default',
                    help="set format of output: plain, json or default"
                    )
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    args = parser.parse_args()
    if args.format == format.DEFAULT:
        format_diff = format.default
    elif args.format == format.PLAIN:
        format_diff = format.plain
    elif args.format == format.JSON:
        format_diff = format.json
    else:
        sys.exit(
            "Wrong output format. Can use only json, plain or default"
        )
    diff = generate_diff(args.first_file, args.second_file, format_diff)
    print(diff)


if __name__ == '__main__':
    main()
