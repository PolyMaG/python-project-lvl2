from gendiff.generate_diff import generate_diff


file = open('./tests/fixtures/correct_json.txt', 'r')
result = file.read()


def test_flat_json_files():
    diff = generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )
    assert result == diff


file.close()
