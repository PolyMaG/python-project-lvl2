import json
import yaml
import os
from gendiff.parsers import (
    get_equal_items,
    get_changed_items,
    get_added_items,
    get_removed_items
)


def generate_diff(first_file, second_file):
    first_file_name, first_file_extension = os.path.splitext(first_file)
    second_file_name, second_file_extension = os.path.splitext(second_file)
    if first_file_extension and second_file_extension == '.json':
        first_file_data = json.load(open(first_file))
        second_file_data = json.load(open(second_file))
    elif first_file_extension and second_file_extension == '.yml':
        first_file_data = yaml.safe_load(open(first_file))
        second_file_data = yaml.safe_load(open(second_file))

    equal_items = get_equal_items(first_file_data, second_file_data)
    changed_added_items, changed_removed_items = get_changed_items(
        first_file_data,
        second_file_data,
    )
    added_items = get_added_items(first_file_data, second_file_data)
    removed_items = get_removed_items(first_file_data, second_file_data)

    diff = (
        '{\n' +
        ''.join(equal_items) + '\n' +
        ''.join(changed_added_items) + '\n' +
        ''.join(changed_removed_items) + '\n' +
        ''.join(removed_items) + '\n' +
        ''.join(added_items) +
        '\n}'
    )
    return diff
