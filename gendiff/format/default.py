import gendiff.parser as diff


def format_obj(value, tab):
    for key, value in value.items():
        return '{}\n{}{}: {}\n{}{}'.format(
            '{', ' ' * (tab + 8), key, value, ' ' * (tab + 4), '}'
            )


def format_val(value, tab):
    if isinstance(value, dict):
        return format_obj(value, tab)
    else:
        return value


def pre_format(ast, tab=0):
    result = ''
    for key, (status, value) in sorted(ast.items()):
        if status == diff.NESTED:
            result += '    {}{}: {}\n{}{}{}\n'.format(
                ' ' * tab, key, '{', pre_format(value, tab + 4), ' ' * (tab + 4), '}' # noqa E501
                )
        elif status == diff.EQUAL:
            result += '    {}{}: {}\n'.format(' ' * tab, key, format_val(value, tab)) # noqa E501
        elif status == diff.ADDED:
            result += '  {}+ {}: {}\n'.format(' ' * tab, key, format_val(value, tab)) # noqa E501
        elif status == diff.REMOVED:
            result += '  {}- {}: {}\n'.format(' ' * tab, key, format_val(value, tab)) # noqa E501
        elif status == diff.MODIFIED:
            old, new = value
            result += '  {}+ {}: {}\n'.format(' ' * tab, key, format_val(new, tab)) # noqa E501
            result += '  {}- {}: {}\n'.format(' ' * tab, key, format_val(old, tab)) # noqa E501
    return result


def format(ast):
    return '{\n' + pre_format(ast) + '}'
