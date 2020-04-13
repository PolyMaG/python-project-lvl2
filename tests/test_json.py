from gendiff.generate_diff import generate_diff


file = open('./tests/fixtures/expected_json.txt', 'r')
EXPECTED = file.read()


def test_json_files():
    actual = generate_diff(
        'json',
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )
    assert EXPECTED == actual


file.close()
