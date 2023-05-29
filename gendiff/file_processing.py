import json
import yaml


def get_file_type(path: str) -> str:
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()
    return file_extension


def parse_file(file, extension):
    if extension == 'json':
        return json.load(file)
    if extension in ('yml', 'yaml'):
        return yaml.load(file, Loader=yaml.Loader)
