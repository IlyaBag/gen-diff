from gendiff.gen_diff import generate_diff


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'

diff = open('tests/fixtures/correct_diff.txt')

def test_generate_diff():
    assert generate_diff(file1, file2) == diff.read()
