import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))  # dict
    file2 = json.load(open(file_path2))

    keys1 = set(file1.keys())
    keys2 = set(file2.keys())
    common_keys = keys1 & keys2

    diff = {}
    for key in common_keys:
        if file1[key] == file2[key]:
            diff[key] = file1[key]
        else:
            diff[f'- {key}'] = file1[key]
            diff[f'+ {key}'] = file2[key]
        keys1.remove(key)
        keys2.remove(key)
    for key1 in keys1:
        diff[f'- {key1}'] = file1[key]
    for key2 in keys2:
        diff[f'+ {key2}'] = file2[key]
    
    return diff
