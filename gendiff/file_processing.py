import json
import yaml


PARSERS = {'json': json.load,
           'yml': lambda obj: yaml.load(obj, Loader=yaml.Loader),
           'yaml': lambda obj: yaml.load(obj, Loader=yaml.Loader)}


def get_file_type(path: str) -> str:
    file_extension = path.rsplit(sep='.', maxsplit=1)[1]
    file_extension.lower()
    return file_extension


def parse_file(file, extension):
    parser = PARSERS[extension]
    return parser(file)
