import json
import yaml
from gendiff.parser import show_diff


def file_parse(path):
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()

    data = {}
    if file_extension == 'json':
        data = json.load(open(path))
    elif file_extension == 'yml' or file_extension == 'yaml':
        data = yaml.load(open(path), Loader=yaml.Loader)
    return data


def generate_diff(file_path1, file_path2):
    file1 = file_parse(file_path1)
    file2 = file_parse(file_path2)

    common_data = set(file1.keys()) | set(file2.keys())
    keys = list(common_data)
    keys.sort()

    diff = []
    for key in keys:
        if key in file1:
            if key in file2:
                if file1[key] == file2[key]:
                    diff.append((f'  {key}', f'{file1[key]}'))
                else:
                    diff.append((f'- {key}', f'{file1[key]}'))
                    diff.append((f'+ {key}', f'{file2[key]}'))
            else:
                diff.append((f'- {key}', f'{file1[key]}'))
        else:
            diff.append((f'+ {key}', f'{file2[key]}'))

    printable_diff = show_diff(diff)
    return printable_diff
