import gendiff.format as format
from gendiff.gendiff import generate_diff


def test_plain_format():
    with open('./tests/fixtures/expected_plain.txt', 'r') as fixture:
        expected = fixture.read()
    with open('./tests/fixtures/expected_plain_extra.txt', 'r') as fixture:
        expected_extra = fixture.read()
    assert expected == generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        format.plain,
    )
    assert expected == generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yaml',
        format.plain,
    )
    assert expected == generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.yaml',
        format.plain,
    )
    assert expected_extra == generate_diff(
        './tests/fixtures/before_extra.yml',
        './tests/fixtures/after_extra.yaml',
        format.plain,
    )
