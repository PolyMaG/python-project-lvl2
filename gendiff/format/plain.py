import gendiff.parser as diff


def format_value(value):
    if isinstance(value, dict):
        return 'complex value'
    else:
        return value


def pre_format(ast, parent=''):
    strings = []
    for key, (status, value) in sorted(ast.items()):
        if status == diff.NESTED:
            strings.append("{}{}".format(parent, pre_format(value, parent=(key + ".")))) # noqa E501
        if status == diff.ADDED:
            strings.append("{}{}' was added with value: '{}'".format(
                parent, key, format_value(value))
                )
        if status == diff.REMOVED:
            strings.append('{}{}\' was removed'.format(parent, key))
        if status == diff.MODIFIED:
            old, new = value
            strings.append("{}{}' was changed. From '{}' to '{}'".format(
                parent, key, format_value(old), format_value(new))
                )
    return '\nProperty \''.join(strings)


def format(ast):
    return 'Property \'' + pre_format(ast)
