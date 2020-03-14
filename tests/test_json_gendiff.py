from gendiff.generate_diff import get_files_data
from gendiff.parsers import generate_diff


file = open('./tests/fixtures/correct_json.txt', 'r')
result = file.read()


def test_flat_json_files():
    first_data, second_data = get_files_data(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )
    assert result == generate_diff(first_data, second_data)


file.close()
