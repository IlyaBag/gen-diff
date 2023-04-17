from gendiff.gen_diff import generate_diff


file1_json = 'tests/fixtures/JSON/file1.json'
file2_json = 'tests/fixtures/JSON/file2.json'
file1_yaml = 'tests/fixtures/YAML/file1.yml'
file2_yaml = 'tests/fixtures/YAML/file2.yml'

correct_diff = open('tests/fixtures/correct_diff.txt').read()
wrong_diff = open('tests/fixtures/wrong_diff.txt').read()


def test_generate_diff_json():
    diff = generate_diff(file1_json, file2_json)
    assert  diff == correct_diff
    assert diff != wrong_diff

def test_generate_diff_yaml():
    diff = generate_diff(file1_yaml, file2_yaml)
    assert  diff == correct_diff
    assert diff != wrong_diff
