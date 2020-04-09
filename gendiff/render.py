def render_obj(value, tabs):
    for key, value in value.items():
        return '{}\n{}{}: {}\n{}{}'.format(
            '{', '    ' * tabs, key, value, '    ' * (tabs - 1), '}'
            )


def render_value(value, tabs):
    if isinstance(value, dict):
        if tabs == 1:
            tabs = 2
        return render_obj(value, tabs)
    else:
        return value


def render_ast(ast):
    result = ''
    tabs = 2
    for item in ast:
        if item.get('type') == 'nested':
            tabs -= 1
            result += '    {}: {}\n{}    {}\n'.format(
                item['key'], '{', render_ast(item['children']), '}'
                )
        elif item.get('type') == 'equal':
            result += '    {}{}: {}\n'.format(
                '  ' * tabs, item['key'], render_value(item['value'], tabs)
                )
        elif item.get('type') == 'added':
            result += '{}+ {}: {}\n'.format(
                '  ' * (tabs + 1), item['key'],
                render_value(item['value'], tabs + 1)
                )
        elif item.get('type') == 'removed':
            result += '{}- {}: {}\n'.format(
                '  ' * (tabs + 1), item['key'],
                render_value(item['value'], tabs + 1)
                )
        elif item.get('type') == 'modified':
            result += '{}  + {}: {}\n'.format(
                '  ' * tabs, item['key'], render_value(item['new_value'], tabs)
                )
            result += '{}  - {}: {}\n'.format(
                '  ' * tabs, item['key'], render_value(item['old_value'], tabs)
                )
    return result
