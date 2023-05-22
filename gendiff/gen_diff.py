import json
import yaml
import gendiff.formatters as gf


FORMAT_ARGS = {'stylish': gf.stylish,
               'plain': gf.plain,
               'json': gf.json_output}


def open_file(path: str):
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()
    return open(path), file_extension


def parse_file(file, extension):
    if extension == 'json':
        return json.load(file)
    if extension in ('yml', 'yaml'):
        return yaml.load(file, Loader=yaml.Loader)


def mark_nested_keys(item):
    if not isinstance(item, dict):
        return item
    marked_dict = {}
    for key in item:
        value = item[key]
        marked_dict[(key, 'nested')] = mark_nested_keys(value)
    return marked_dict


def compare_files(item1: dict, item2: dict) -> dict:
    item1_keys = set(item1.keys())
    item2_keys = set(item2.keys())

    mutual_keys = item1_keys & item2_keys
    item1_unique_keys = item1_keys - item2_keys
    item2_unique_keys = item2_keys - item1_keys

    diff = {}

    for key in item1_unique_keys:
        diff[(key, 'deleted')] = mark_nested_keys(item1[key])

    for key in item2_unique_keys:
        diff[(key, 'added')] = mark_nested_keys(item2[key])

    for key in mutual_keys:
        value1 = item1[key]
        value2 = item2[key]
        if value1 == value2:
            diff[(key, 'same')] = mark_nested_keys(value1)
        else:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff[(key, 'nesting')] = compare_files(value1, value2)
            else:
                diff[(key, 'changed')] = {
                    ('changed', 'from'): mark_nested_keys(value1),
                    ('changed', 'to'): mark_nested_keys(value2)
                }

    return diff


def generate_diff(file_path1, file_path2, output='stylish'):
    file1, file_type1 = open_file(file_path1)
    file2, file_type2 = open_file(file_path2)

    data1 = parse_file(file1, file_type1)
    data2 = parse_file(file2, file_type2)

    diff = compare_files(data1, data2)

    formatter = FORMAT_ARGS.get(output, lambda _: 'Unknown output format')

    return formatter(diff)
