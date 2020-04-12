import json
import yaml
import os
from gendiff.parser import build_ast
from gendiff.formatters.jsontxt_formatter import to_jsontxt_format
from gendiff.formatters.plain_formatter import to_plain_format


def get_file_data(first_file, second_file):
    first_file_name, first_file_extension = os.path.splitext(first_file)
    second_file_name, second_file_extension = os.path.splitext(second_file)
    if first_file_extension and second_file_extension == '.json':
        first_file_data = json.load(open(first_file))
        second_file_data = json.load(open(second_file))
    elif first_file_extension and second_file_extension == '.yml':
        first_file_data = yaml.safe_load(open(first_file))
        second_file_data = yaml.safe_load(open(second_file))
    else:
        print('Wrong file format')
    return first_file_data, second_file_data


def generate_diff(format, first_file, second_file):
    first_file_data, second_file_data = get_file_data(first_file, second_file)
    ast = build_ast(first_file_data, second_file_data)
    if format == 'jsontxt':
        diff = '{\n' + to_jsontxt_format(ast) + '}'
    elif format == 'plain':
        diff = to_plain_format(ast)
    return diff
