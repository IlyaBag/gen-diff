from gendiff.gen_diff import generate_diff


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


def test_generate_diff_json():
    diff = generate_diff(file1_json, file2_json)
    assert  diff == correct_diff
    assert diff != wrong_diff

def test_generate_diff_yaml():
    diff = generate_diff(file1_yaml, file2_yaml)
    assert  diff == correct_diff
    assert diff != wrong_diff

def test_generate_diff_json_nested():
    diff = generate_diff(file1_json_nested, file2_json_nested)
    assert  diff == correct_nested_diff

def test_generate_diff_yaml_nested():
    diff = generate_diff(file1_yaml_nested, file2_yaml_nested)
    assert  diff == correct_nested_diff

def test_generate_diff_json_plain():
    diff = generate_diff(file1_json_nested, file2_json_nested, 'plain')
    assert  diff == correct_plain_diff

def test_generate_diff_yaml_plain():
    diff = generate_diff(file1_yaml_nested, file2_yaml_nested, 'plain')
    assert  diff == correct_plain_diff
