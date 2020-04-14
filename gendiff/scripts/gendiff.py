#!/usr/bin/env python3
from gendiff.diff import generate_diff
import argparse
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format',
                    help="set format of output: json, plain, jsontxt")
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    args = parser.parse_args()
    diff = generate_diff(args.format, args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
