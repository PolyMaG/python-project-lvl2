from gendiff.generate_diff import generate_diff


file_yml = open('./tests/fixtures/correct_yml.txt', 'r')
result = file_yml.read()


def test_flat_yml_files():
    diff = generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )
    assert result == diff


file_yml.close()
