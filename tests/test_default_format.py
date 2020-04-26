import gendiff.format as format
from gendiff.diff import generate_diff


def test_default_format():
    with open('./tests/fixtures/expected_nested.txt', 'r') as expected_nested:
        with open('./tests/fixtures/expected_flat.txt', 'r') as expected_flat:
            with open('./tests/fixtures/expected_extra_nested.txt', 'r') as expected_extra_nested:
                expected_nested = expected_nested.read()
                expected_flat = expected_flat.read()
                expected_extra_nested = expected_extra_nested.read()
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
