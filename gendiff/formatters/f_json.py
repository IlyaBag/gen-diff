import json


def untuple(data):
    if not isinstance(data, dict):
        return data
    untupled_data = {}
    for key in data:
        untupled_data[f'{key[0]}, {key[1]}'] = untuple(data[key])
    return untupled_data


def json_output(data):
    valid_data = untuple(data)
    return json.dumps(valid_data, sort_keys=True, indent=4)
