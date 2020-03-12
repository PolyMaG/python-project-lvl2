#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff, get_paths
import argparse
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('-f', '--format', help="set format of output")
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    args = parser.parse_args()
    first_file, second_file = get_paths(args.first_file, args.second_file)
    diff = generate_diff(first_file, second_file)
    print(diff)


if __name__ == '__main__':
    main()
