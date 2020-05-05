import gendiff.format as format
from gendiff.gendiff import generate_diff


def test_default_format():
    with open('./tests/fixtures/expected_nested.txt', 'r') as fixture:
        expected_nested = fixture.read()
    with open('./tests/fixtures/expected_flat.txt', 'r') as fixture:
        expected_flat = fixture.read()
    with open('./tests/fixtures/expected_extra_nested.txt', 'r') as fixture:
        expected_extra_nested = fixture.read()
    assert expected_nested == generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        format.default,
    )
    assert expected_nested == generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yaml',
        format.default,
    )
    assert expected_nested == generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.yaml',
        format.default,
    )
    assert expected_flat == generate_diff(
        './tests/fixtures/before_flat.json',
        './tests/fixtures/after_flat.json',
        format.default,
    )
    assert expected_flat == generate_diff(
        './tests/fixtures/before_flat.yml',
        './tests/fixtures/after_flat.yaml',
        format.default,
    )
    assert expected_flat == generate_diff(
        './tests/fixtures/before_flat.json',
        './tests/fixtures/after_flat.yaml',
        format.default,
    )
    assert expected_extra_nested == generate_diff(
        './tests/fixtures/before_extra_nested.yml',
        './tests/fixtures/after_extra_nested.yaml',
        format.default,
    )
