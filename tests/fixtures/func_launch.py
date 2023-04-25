from gendiff import generate_diff


print('json')
print(generate_diff('tests/fixtures/flat/file1.json', 'tests/fixtures/flat/file2.json'))
print()
print('yaml')
print(generate_diff('tests/fixtures/flat/file1.yml', 'tests/fixtures/flat/file2.yml'))
print()
print('nested json')
print(generate_diff('tests/fixtures/nested/file1.json', 'tests/fixtures/nested/file2.json'))
print()
print('nested yaml')
print(generate_diff('tests/fixtures/nested/file1.yml', 'tests/fixtures/nested/file2.yml'))
