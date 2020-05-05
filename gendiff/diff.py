TYPES = (NESTED, EQUAL, MODIFIED, REMOVED, ADDED) = (
    'nested', 'equal', 'modified', 'removed', 'added'
)


def build(first_data, second_data):
    diff = {}
    common_items = first_data.keys() & second_data.keys()
    removed_items = first_data.keys() - second_data.keys()
    added_items = second_data.keys() - first_data.keys()
    for item in common_items:
        value1 = first_data[item]
        value2 = second_data[item]
        if isinstance(value1, dict) and isinstance(value2, dict):
            value = (NESTED, build(value1, value2))
        elif value1 == value2:
            value = (EQUAL, value1)
        else:
            value = (MODIFIED, (value1, value2))
        diff[item] = value
    for item in removed_items:
        diff[item] = (REMOVED, first_data[item])
    for item in added_items:
        diff[item] = (ADDED, second_data[item])
    return diff
