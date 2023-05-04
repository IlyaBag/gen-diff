def fix_syntax(string):
    if string in ('True', 'False'):
        return ' ' + string.lower()
    if string == 'None':
        return ' null'
    if string == '':
        return ''
    return ' ' + string


def is_leaf_node(item):
    if '_state_' in item and '_value_' in item:
        return True
    return False


def stylish(diff, replacer=' ', indent_length=4):  # noqa: C901
    def inner(cur_diff, accum_indent_length):

        def get_printable_value(data, depth=0):
            if isinstance(data, dict):
                data_keys = list(data.keys())
                data_keys.sort()

                additional_indent = replacer * indent_length
                nested_indent = full_cur_indent + additional_indent * depth
                deep_nested_indent = nested_indent + additional_indent

                printable_value = ' {'
                for key in data_keys:
                    data_val = get_printable_value(data[key], depth + 1)
                    printable_value += f'\n{deep_nested_indent}{key}:{data_val}'
                printable_value += f'\n{nested_indent}{"}"}'
            else:
                printable_value = fix_syntax(str(data))
            return printable_value

        cur_indent_length = accum_indent_length + indent_length
        accum_indent = replacer * accum_indent_length
        cur_indent = replacer * (cur_indent_length - 2)
        full_cur_indent = replacer * (cur_indent_length)

        printable_diff = '{'

        cur_keys = list(cur_diff.keys())
        cur_keys.sort()
        for key in cur_keys:
            cur_value = cur_diff[key]
            if is_leaf_node(cur_value):
                # преоразование в строку
                state = cur_value['_state_']
                value = get_printable_value(cur_value['_value_'])
                printable_diff += f'\n{cur_indent}{state} {key}:{value}'
                if '_value2_' in cur_value:
                    state2 = cur_value['_state2_']
                    value2 = get_printable_value(cur_value['_value2_'])
                    printable_diff += f'\n{cur_indent}{state2} {key}:{value2}'
            else:
                # рекурсивный вызов
                value = inner(cur_value, cur_indent_length)
                printable_diff += f'\n{full_cur_indent}{key}: {value}'

        printable_diff += f'\n{accum_indent}{"}"}'
        return printable_diff
    return inner(diff, 0)
