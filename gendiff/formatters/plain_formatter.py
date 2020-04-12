def format_value(value):
    if isinstance(value, dict):
        return 'complex value'
    else:
        return value


def to_plain_format(ast, parent=''):
    result = ''
    for item in ast:
        if item.get('type') == 'nested':
            if result:
                result += '\n'
            result += "{}{}".format(
                parent, to_plain_format(item['children'],
                                        parent=(item['key'] + "."))
                )
        else:
            if item.get('type') == 'added':
                if result:
                    result += '\n'
                result += "Property '{}{}' was added with value: '{}'".format(
                    parent, item['key'], format_value(item['value'])
                    )
            if item.get('type') == 'removed':
                if result:
                    result += '\n'
                result += 'Property \'{}{}\' was removed'.format(
                    parent, item['key']
                    )
            if item.get('type') == 'modified':
                if result:
                    result += '\n'
                result += "Property '{}{}' was changed. From '{}' to '{}'".format( # noqa E501
                    parent, item['key'], format_value(item['old_value']),
                    format_value(item['new_value'])
                    )
    return result
