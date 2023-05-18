import json
import yaml
import gendiff.formatters as gf


FORMAT_ARGS = {'stylish': gf.stylish,
               'plain': gf.plain,
               'json': gf.json_output
               }


def file_parse(path):
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()

    data = None
    if file_extension == 'json':
        data = json.load(open(path))
    elif file_extension == 'yml' or file_extension == 'yaml':
        data = yaml.load(open(path), Loader=yaml.Loader)
    return data


def nested_keys_marker(item):
    if not isinstance(item, dict):
        return item
    marked_dict = {}
    for key in item:
        value = item[key]
        marked_dict[(key, 'nested')] = nested_keys_marker(value)
    return marked_dict


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
            diff[(key, 'deleted')] = nested_keys_marker(data1[key])

        for key in data2_unique_keys:
            diff[(key, 'added')] = nested_keys_marker(data2[key])

        for key in mutual_keys:
            value1 = data1[key]
            value2 = data2[key]
            if value1 == value2:
                diff[(key, 'same')] = nested_keys_marker(value1)
            else:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff[(key, 'nesting')] = inner(value1, value2)
                else:
                    diff[(key, 'changed')] = (nested_keys_marker(value1),
                                              nested_keys_marker(value2))

        return diff

    formatter = FORMAT_ARGS.get(output, lambda _: 'Unknown output format')

    try:
        return formatter(inner(file1, file2))
    except AttributeError:
        return 'Unknown file type'
