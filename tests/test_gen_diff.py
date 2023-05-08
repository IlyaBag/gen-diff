from gendiff.gen_diff import generate_diff
import json
import pytest


file1_json = 'tests/fixtures/flat/file1.json'
file2_json = 'tests/fixtures/flat/file2.json'
file1_yaml = 'tests/fixtures/flat/file1.yml'
file2_yaml = 'tests/fixtures/flat/file2.yml'
file1_json_nested = 'tests/fixtures/nested/file1.json'
file2_json_nested = 'tests/fixtures/nested/file2.json'
file1_yaml_nested = 'tests/fixtures/nested/file1.yml'
file2_yaml_nested = 'tests/fixtures/nested/file2.yml'

correct_diff = open('tests/fixtures/correct_diff.txt').read()
wrong_diff = open('tests/fixtures/wrong_diff.txt').read()
correct_nested_diff = open('tests/fixtures/correct_nested_diff.txt').read()
correct_plain_diff = open('tests/fixtures/correct_plain_diff.txt').read()


@pytest.mark.parametrize(
    ('first_file', 'second_file', 'expected_diff'),
    (
        (file1_json, file2_json, correct_diff),
        (file1_yaml, file2_yaml, correct_diff),
        (file1_json_nested, file2_json_nested, correct_nested_diff),
        (file1_yaml_nested, file2_yaml_nested, correct_nested_diff),
        (file1_json, correct_diff, 'Unknown file type'),
    )
)
def test_generate_diff(first_file, second_file, expected_diff):
    diff = generate_diff(first_file, second_file)
    assert diff == expected_diff


@pytest.mark.parametrize(
    ('first_file', 'second_file', 'formatter', 'expected_diff'),
    (
        (file1_json_nested, file2_json_nested, 'stylish', correct_nested_diff),
        (file1_json_nested, file2_json_nested, 'plain', correct_plain_diff),
        (file1_yaml_nested, file2_yaml_nested, 'plain', correct_plain_diff),
        (file1_json, file2_json, 'failish', 'Unknown output format')
    )
)
def test_generate_diff_formatter(
    first_file, second_file, formatter, expected_diff
):
    diff = generate_diff(first_file, second_file, formatter)
    assert diff == expected_diff


def test_generate_diff_output_json():
    diff = generate_diff(file1_yaml_nested, file2_yaml_nested, 'json')
    assert json.loads(diff)


# def test_generate_diff_wrong_file_type():
#     with pytest.raises(AttributeError):
#         generate_diff(file1_json, correct_diff)
