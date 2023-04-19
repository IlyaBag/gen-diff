import json
import yaml


# def get_file_extension(path):
#     file_extension = path.rsplit(sep='.', maxsplit=1)[1]
#     return file_extension.lower()
def file_parse(path):
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()

    data = {}
    if file_extension == 'json':
        data = json.load(open(path))
    elif file_extension == 'yml' or file_extension == 'yaml':
        data = yaml.load(open(path), Loader=yaml.Loader)
    return data, file_extension


def get_data(file_path1, file_path2):
    file1, file1_ext = file_parse(file_path1)
    file2, file2_ext = file_parse(file_path2)
    file_extension = 'yaml'
    if file1_ext == 'json' and file2_ext == 'json':
        file_extension = 'json'
    return file1, file2, file_extension


def show_diff(diff, file_format):
    if file_format == 'json':
        return json.dumps(diff, indent=2).replace('"', '')
    elif file_format == 'yaml':
        return yaml.dump(diff,
                         default_flow_style=False,
                         width=float('INF'),
                         sort_keys=False
                         ).replace("'", "")
    else:
        return 'Unknown file format'
