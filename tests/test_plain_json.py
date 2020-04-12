from gendiff.generate_diff import generate_diff


file = open('./tests/fixtures/expected_plain.txt', 'r')
EXPECTED = file.read()


def test_plain_json_files():
    actual = generate_diff(
        'plain',
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )
    assert EXPECTED == actual


file.close()
