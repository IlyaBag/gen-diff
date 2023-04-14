from gendiff.gen_diff import generate_diff


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'

diff = '''{
  - follow: false,
    host: hexlet.io,
  + memorized: true,
  - proxy: 123.234.53.22,
  - timeout: 50,
  + timeout: 20,
  + verbose: true
}'''

def test_generate_diff():
    assert generate_diff(file1, file2) == diff
