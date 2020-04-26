import json
import yaml
import os
import sys
from gendiff.parser import build_ast


def get_file_data(file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        file_data = json.load(open(file))
    elif file_extension == '.yml' or file_extension == '.yaml':
        file_data = yaml.safe_load(open(file))
    else:
        sys.exit('Wrong file format. Can use only .json or .yml/.yaml files')
    return file_data


def generate_diff(first_file, second_file, format_diff):
    first_file_data = get_file_data(first_file)
    second_file_data = get_file_data(second_file)
    ast = build_ast(first_file_data, second_file_data)
    formatted_diff = format_diff(ast)
    return formatted_diff
