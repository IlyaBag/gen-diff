import yaml#, json


# def get_file_extension(path):
#     file_extension = path.rsplit(sep='.', maxsplit=1)[1]
#     return file_extension.lower()

def get_data(file_path1, file_path2):
    file1 = yaml.load(open(file_path1), Loader=yaml.Loader)  # dict
    file2 = yaml.load(open(file_path2), Loader=yaml.Loader)

    common_data = set(file1.keys()) | set(file2.keys())
    keys = list(common_data)
    keys.sort()
    return file1, file2, keys


def show_diff(diff):
    # if file_format is 'json':
    #     return json.dumps(diff, indent=2).replace('"', '')
    # elif file_format is 'yml' or file_format is 'yaml':
    return yaml.dump(diff, default_flow_style=False, width=float('INF'), sort_keys=False).replace("'", "")
    # else:
    #     return 'Unknown file format'
