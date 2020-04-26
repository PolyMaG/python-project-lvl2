import json
import gendiff.format as format
from gendiff.diff import generate_diff


def test_json_format():
    expected = json.load(open('./tests/fixtures/expected.json'))
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
