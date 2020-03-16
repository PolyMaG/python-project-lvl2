def get_equal_items(first_data, second_data):
    equal_items = []
    for key, value in first_data.items() & second_data.items():
        equal_items.append('  ' + key + ': ' + str(value))
    return equal_items


def get_changed_items(first_data, second_data):
    changed_added_items = []
    changed_removed_items = []
    for key in first_data.keys() & second_data.keys():
        if first_data.get(key) != second_data.get(key):
            changed_added_items.append(
                '+ ' + key + ': ' + str(second_data.get(key))
            )
            changed_removed_items.append(
                '- ' + key + ': ' + str(first_data.get(key))
            )
    return changed_added_items, changed_removed_items


def get_removed_items(first_data, second_data):
    removed_items = []
    for key in first_data.keys() - second_data.keys():
        removed_items.append('- ' + key + ': ' + str(first_data.get(key)))
    return removed_items


def get_added_items(first_data, second_data):
    added_items = []
    for key in second_data.keys() - first_data.keys():
        added_items.append('+ ' + key + ': ' + str(second_data.get(key)))
    return added_items
