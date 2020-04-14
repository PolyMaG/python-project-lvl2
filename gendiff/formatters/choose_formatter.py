from gendiff.formatters.jsontxt_formatter import to_jsontxt_format
from gendiff.formatters.plain_formatter import to_plain_format
from gendiff.formatters.json_formatter import to_json_format


def choose_format(format, ast):
    if format == 'jsontxt':
        formatted_diff = '{\n' + to_jsontxt_format(ast) + '}'
    elif format == 'plain':
        formatted_diff = to_plain_format(ast)
    elif format == 'json':
        formatted_diff = to_json_format(ast)
    else:
        formatted_diff = '{\n' + to_jsontxt_format(ast) + '}'
    return formatted_diff
