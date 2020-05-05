import json
import gendiff.format as format
from gendiff.gendiff import generate_diff


def test_json_format():
    with open('./tests/fixtures/expected.json') as fixture:
        expected = json.load(fixture)
    assert expected == json.loads(generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        format.json,
    ))
    assert expected == json.loads(generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yaml',
        format.json,
    ))
    assert expected == json.loads(generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.yaml',
        format.json,
    ))
