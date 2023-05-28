import json
import yaml


def open_file(path: str):
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()
    return open(path), file_extension


def parse_file(file, extension):
    if extension == 'json':
        return json.load(file)
    if extension in ('yml', 'yaml'):
        return yaml.load(file, Loader=yaml.Loader)
