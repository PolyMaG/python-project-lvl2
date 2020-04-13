def build_ast(first_data, second_data):
    ast = []
    common_items = sorted(first_data.keys() & second_data.keys())
    removed_items = sorted(first_data.keys() - second_data.keys())
    added_items = sorted(second_data.keys() - first_data.keys())
    for item in common_items:
        if isinstance(first_data[item], dict) and isinstance(second_data[item], dict): # noqa E501
            ast.append(
              {'type': 'nested', 'key': item,
               'children': build_ast(first_data[item], second_data[item])}
              )
        elif first_data[item] == second_data[item]:
            ast.append({'type': 'equal', 'key': item, 'value': first_data[item]}) # noqa E501
        else:
            ast.append(
              {'type': 'modified', 'key': item,
               'old_value': first_data[item],
               'new_value': second_data[item]}
               )
    for item in removed_items:
        ast.append({'type': 'removed', 'key': item, 'value': first_data[item]})
    for item in added_items:
        ast.append({'type': 'added', 'key': item, 'value': second_data[item]})
    return ast
