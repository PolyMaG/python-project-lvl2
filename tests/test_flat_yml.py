from gendiff.generate_diff import generate_diff


file_yml = open('./tests/fixtures/expected_flat.txt', 'r')
EXPECTED = file_yml.read()


def test_flat_yml_files():
    actual = generate_diff(
        'jsontxt',
        './tests/fixtures/before_flat.yml',
        './tests/fixtures/after_flat.yml'
    )
    assert EXPECTED == actual


file_yml.close()
