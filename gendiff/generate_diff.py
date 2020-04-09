import json
import yaml
import os
from gendiff.parser import build_ast
from gendiff.render import render_ast


def generate_diff(first_file, second_file):
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

    ast = build_ast(first_file_data, second_file_data)
    diff = render_ast(ast)
    return '{\n' + diff + '}'
