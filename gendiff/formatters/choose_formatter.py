from gendiff.formatters.jsontxt_formatter import to_jsontxt_format
from gendiff.formatters.plain_formatter import to_plain_format
from gendiff.formatters.json_formatter import to_json_format


def to_format(format, ast):
    if format == 'jsontxt':
        diff_to_format = '{\n' + to_jsontxt_format(ast) + '}'
    elif format == 'plain':
        diff_to_format = to_plain_format(ast)
    elif format == 'json':
        diff_to_format = to_json_format(ast)
    return diff_to_format
