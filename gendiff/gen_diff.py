from gendiff.file_processing import get_file_type, parse_file
from gendiff.data_comparison import compare_files
import gendiff.formatters as gf


FORMAT_ARGS = {'stylish': gf.stylish,
               'plain': gf.plain,
               'json': gf.json_output}


def generate_diff(file_path1, file_path2, output='stylish'):
    file_type1 = get_file_type(file_path1)
    file_type2 = get_file_type(file_path2)

    file1 = open(file_path1)
    file2 = open(file_path2)

    data1 = parse_file(file1, file_type1)
    data2 = parse_file(file2, file_type2)

    diff = compare_files(data1, data2)

    formatter = FORMAT_ARGS.get(output, lambda _: 'Unknown output format')

    return formatter(diff)
