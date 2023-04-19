from gendiff import generate_diff


print('json')
print(generate_diff('tests/fixtures/JSON/file1.json', 'tests/fixtures/JSON/file2.json'))
print()
print('yaml')
print(generate_diff('tests/fixtures/YAML/file1.yml', 'tests/fixtures/YAML/file2.yml'))
