from gendiff.generate_diff import generate_diff


file_yml = open('./tests/fixtures/expected_yml.txt', 'r')
EXPECTED = file_yml.read()


def test_flat_yml_files():
    actual = generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )
    assert EXPECTED == actual


file_yml.close()
