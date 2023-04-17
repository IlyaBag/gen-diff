from gendiff.parser import get_data, show_diff


def generate_diff(file_path1, file_path2):
    file1, file2, keys = get_data(file_path1, file_path2)
    # file1 = json.load(open(file_path1))  # dict
    # file2 = json.load(open(file_path2))

    # keys = list(file1.keys())
    # keys2 = list(file2.keys())
    # keys.extend(keys2)
    # keys.sort()

    diff = {}
    for key in keys:
        if key in file1:
            if key in file2:
                if file1[key] == file2[key]:
                    diff[f'  {key}'] = file1[key]
                else:
                    diff[f'- {key}'] = file1[key]
                    diff[f'+ {key}'] = file2[key]
            else:
                diff[f'- {key}'] = file1[key]
        else:
            diff[f'+ {key}'] = file2[key]

    # return json.dumps(diff, indent=2).replace('"', '')
    return show_diff(diff)
