import json


def json_output(data):
    output_data = json.dumps(data, indent=4)
    return output_data
