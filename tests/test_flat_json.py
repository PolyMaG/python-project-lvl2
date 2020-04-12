from gendiff.generate_diff import generate_diff


file = open('./tests/fixtures/expected_flat.txt', 'r')
EXPECTED = file.read()


def test_flat_json_files():
    actual = generate_diff(
        'jsontxt',
        './tests/fixtures/before_flat.json',
        './tests/fixtures/after_flat.json'
    )
    assert EXPECTED == actual


file.close()
