import json
import yaml
from gendiff.formatters import *  # noqa: F403


format_args = {
    'stylish': stylish,  # noqa: F405
    'plain': plain,  # noqa: F405
    'json': json_output,  # noqa: F405
}


def file_parse(path):
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()

    data = {}
    if file_extension == 'json':
        data = json.load(open(path))
    elif file_extension == 'yml' or file_extension == 'yaml':
        data = yaml.load(open(path), Loader=yaml.Loader)
    return data


def generate_diff(file_path1, file_path2, output='stylish'):  # noqa: C901
    file1 = file_parse(file_path1)
    file2 = file_parse(file_path2)

    def inner(data1, data2):
        data1_keys = set(data1.keys())
        data2_keys = set(data2.keys())

        mutual_keys = data1_keys & data2_keys
        data1_unique_keys = data1_keys - data2_keys
        data2_unique_keys = data2_keys - data1_keys

        diff = {}
        for key in data1_unique_keys:
            diff[key] = {
                '_state_': '-',
                '_value_': data1[key]
            }
        for key in data2_unique_keys:
            diff[key] = {
                '_state_': '+',
                '_value_': data2[key]
            }
        for key in mutual_keys:
            value1 = data1[key]
            value2 = data2[key]
            if value1 == value2:
                diff[key] = {
                    '_state_': ' ',
                    '_value_': value1
                }
            else:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff[key] = inner(value1, value2)
                else:
                    diff[key] = {
                        '_state_': '-',
                        '_value_': value1,
                        '_state2_': '+',
                        '_value2_': value2
                    }

        return diff
    formatter = format_args.get(output, lambda _: 'Unknown output format')
    return formatter(inner(file1, file2))
