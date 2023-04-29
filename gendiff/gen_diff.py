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

    # def inner(file1, file2):
    #     common_data = set(file1.keys()) | set(file2.keys())
    #     keys = list(common_data)
    #     keys.sort()

    #     diff = {}
    #     for key in keys:
    #         val1 = file1[key]
    #         val2 = file2[key]
    #         if key in file1:
    #             if key in file2:
    #                 if val1 == val2:
    #                     if isinstance(val1, dict):
    #                         inner_diff = inner(val1, val2)
    #                         diff[f'  {key}'] = inner_diff
    #                     else:
    #                         diff[f'  {key}'] = f'{val1}'
    #                 else:
    #                     if isinstance(val1, dict):
    #                         if isinstance(val2, dict):
    #                             inner_diff = inner(val1, val2)
    #                             diff[f'  {key}'] = inner_diff
    #                         else:
    #                             inner_diff = inner(val1, val1)
    #                             diff[f'- {key}'] = inner_diff
    #                             diff[f'+ {key}'] = f'{val2}'
    #                     elif isinstance(val2, dict):
    #                         inner_diff = inner(val2, val2)
    #                         diff[f'- {key}'] = f'{val1}'
    #                         diff[f'+ {key}'] = inner_diff
    #                     else:
    #                         diff[f'- {key}'] = f'{val1}'
    #                         diff[f'+ {key}'] = f'{val2}'
    #             else:
    #                 if isinstance(val1, dict):
    #                     inner_diff = inner(val1, val1)
    #                     diff[f'- {key}'] = inner_diff
    #                 else:
    #                     diff[f'- {key}'] = f'{val1}'
    #         else:
    #             if isinstance(val2, dict):
    #                 inner_diff = inner(val2, val2)
    #                 diff[f'+ {key}'] = inner_diff
    #             else:
    #                 diff[f'+ {key}'] = f'{val2}'
    # diff = []
    # for key in keys:
    #     if key in file1:
    #         if key in file2:
    #             if file1[key] == file2[key]:
    #                 diff.append((f'  {key}', f'{file1[key]}'))
    #             else:
    #                 diff.append((f'- {key}', f'{file1[key]}'))
    #                 diff.append((f'+ {key}', f'{file2[key]}'))
    #         else:
    #             diff.append((f'- {key}', f'{file1[key]}'))
    #     else:
    #         diff.append((f'+ {key}', f'{file2[key]}'))

        # printable_diff = show_diff(diff)
        return diff
    return show_diff(inner(file1, file2))
    # return inner(file1, file2)
