from gendiff.generate_diff import get_files_data
from gendiff.parsers import generate_diff


file_yml = open('./tests/fixtures/correct_yml.txt', 'r')
result = file_yml.read()


def test_flat_yml_files():
    first_data, second_data = get_files_data(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )
    assert result == generate_diff(first_data, second_data)


file_yml.close()
