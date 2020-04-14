from gendiff.diff import generate_diff


file = open('./tests/fixtures/expected_plain.txt', 'r')
EXPECTED = file.read()


def test_plain_yml_files():
    actual = generate_diff(
        'plain',
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )
    assert EXPECTED == actual


file.close()
