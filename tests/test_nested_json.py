from gendiff.generate_diff import generate_diff


file = open('./tests/fixtures/expected_nested_json.txt', 'r')
EXPECTED = file.read()


def test_nested_json_files():
    actual = generate_diff(
        './tests/fixtures/before_nested.json',
        './tests/fixtures/after_nested.json'
    )
    assert EXPECTED == actual


file.close()
