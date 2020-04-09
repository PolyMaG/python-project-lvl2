def build_ast(first_data, second_data):
    ast = []
    for k in first_data.keys():
        if k in second_data.keys():
            if isinstance(first_data[k], dict) and isinstance(
              second_data[k], dict
              ):
                ast.append(
                  {'type': 'nested', 'key': k,
                   'children': build_ast(first_data[k], second_data[k])}
                  )
            elif first_data[k] == second_data[k]:
                ast.append({'type': 'equal', 'key': k, 'value': first_data[k]})
            else:
                ast.append(
                  {'type': 'modified', 'key': k,
                   'old_value': first_data[k], 'new_value': second_data[k]}
                  )
        else:
            ast.append({'type': 'removed', 'key': k, 'value': first_data[k]})
    for k in second_data.keys():
        if k not in first_data.keys():
            ast.append(
              {'type': 'added', 'key': k, 'value': second_data[k]}
              )
    return ast
