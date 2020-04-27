TYPES = (NESTED, EQUAL, MODIFIED, REMOVED, ADDED) = (
        'nested', 'equal', 'modified', 'removed', 'added'
        )


def build_ast(first_data, second_data):
    ast = {}
    common_items = first_data.keys() & second_data.keys()
    removed_items = first_data.keys() - second_data.keys()
    added_items = second_data.keys() - first_data.keys()
    for item in common_items:
        value1 = first_data[item]
        value2 = second_data[item]
        if isinstance(value1, dict) and isinstance(value2, dict):
            ast[item] = (NESTED, build_ast(value1, value2))
        elif value1 == value2:
            ast[item] = (EQUAL, value1)
        else:
            ast[item] = (MODIFIED, (value1, value2))
    for item in removed_items:
        ast[item] = (REMOVED, first_data[item])
    for item in added_items:
        ast[item] = (ADDED, second_data[item])
    return ast
