from gendiff import generate_diff


print('***json***')
jf = generate_diff('tests/fixtures/flat/file1.json', 'tests/fixtures/flat/file2.json')
print(jf)

print()

print('***yaml***')
yf = generate_diff('tests/fixtures/flat/file1.yml', 'tests/fixtures/flat/file2.yml')
print(yf)

print('-' * 80)
print(f'Diffs equal -- {jf == yf}')
print('-' * 80)

print()

print('***nested json***')
jn = generate_diff('tests/fixtures/nested/file1.json', 'tests/fixtures/nested/file2.json')
print(jn)

print()

print('***nested yaml***')
yn = generate_diff('tests/fixtures/nested/file1.yml', 'tests/fixtures/nested/file2.yml')
print(yn)

print('-' * 80)
print(f'Diffs equal -- {jn == yn}')
print('-' * 80)
