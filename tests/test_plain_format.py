import gendiff.format as format
from gendiff.diff import generate_diff


def test_plain_format():
    with open('./tests/fixtures/expected_plain.txt', 'r') as expected:
        with open('./tests/fixtures/expected_plain_extra.txt', 'r') as expected_extra:
            expected = expected.read()
            expected_extra = expected_extra.read()
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
