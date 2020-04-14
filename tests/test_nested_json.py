from gendiff.diff import generate_diff


file = open('./tests/fixtures/expected_nested.txt', 'r')
EXPECTED = file.read()


def test_nested_json_files():
    actual = generate_diff(
        'jsontxt',
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )
    assert EXPECTED == actual


file.close()
