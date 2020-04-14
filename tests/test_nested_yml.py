from gendiff.diff import generate_diff


file = open('./tests/fixtures/expected_nested.txt', 'r')
EXPECTED = file.read()


def test_nested_yml_files():
    actual = generate_diff(
        'jsontxt',
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )
    assert EXPECTED == actual


file.close()
