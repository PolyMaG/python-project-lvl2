from gendiff.generate_diff import generate_diff, get_paths


file = open('./tests/fixtures/correct_answer.txt', 'r')
result = file.read()


def test_flat_files():
    first_file, second_file = get_paths(
        './tests/fixtures/file1.json',
        './tests/fixtures/file2.json'
    )
    assert result == generate_diff(first_file, second_file)


file.close()
