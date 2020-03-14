#!/usr/bin/env python3
from gendiff.generate_diff import get_files_data
from gendiff.parsers import generate_diff
import argparse
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format', help="set format of output")
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    args = parser.parse_args()
    first_data, second_data = get_files_data(args.first_file, args.second_file)
    diff = generate_diff(first_data, second_data)
    print(diff)


if __name__ == '__main__':
    main()
