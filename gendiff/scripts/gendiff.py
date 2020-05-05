#!/usr/bin/env python3
import argparse
import gendiff.format as format
from gendiff.gendiff import generate_diff


def formatter(name):
    if name == format.DEFAULT:
        return format.default
    elif name == format.PLAIN:
        return format.plain
    elif name == format.JSON:
        return format.json
    else:
        raise argparse.ArgumentTypeError(
            "Unknown output format: {}. Use one of this: {}".format(
                name,
                ', '.join(format.FORMATTERS),
            )
        )


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    '-f', '--format',
    default=format.DEFAULT,
    help="set format of output",
    type=formatter,
)
parser.add_argument('first_file')
parser.add_argument('second_file')


def main():
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
