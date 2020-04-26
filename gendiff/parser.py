TYPES = (NESTED, EQUAL, MODIFIED, REMOVED, ADDED) = (
        'nested', 'equal', 'modified', 'removed', 'added'
        )


def build_ast(first_data, second_data):
    ast = {}
    common_items = first_data.keys() & second_data.keys()
    removed_items = first_data.keys() - second_data.keys()
    added_items = second_data.keys() - first_data.keys()
    for item in common_items:
        first_value = first_data[item]
        second_value = second_data[item]
        if isinstance(first_value, dict) and isinstance(second_value, dict):
            ast[item] = (NESTED, build_ast(first_value, second_value))
        elif first_value == second_value:
            ast[item] = (EQUAL, first_value)
        else:
            ast[item] = (MODIFIED, (first_value, second_value))
    for item in removed_items:
        ast[item] = (REMOVED, first_data[item])
    for item in added_items:
        ast[item] = (ADDED, second_data[item])
    return ast
