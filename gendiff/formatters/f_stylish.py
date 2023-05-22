STATES = {'deleted': '- ',
          'added': '+ ',
          'same': '  ',
          'nesting': '  ',
          'nested': '  '}


def fix_syntax(item):
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    return item


def stylish(data, replacer=' ', indent_length=4, depth=1):
    if not isinstance(data, dict):
        return fix_syntax(data)

    indent = replacer * (indent_length * depth - 2)

    printable_diff = '{'

    keys = list(data.keys())
    keys.sort()

    for key in keys:
        diff_key, state = key
        raw_value = data[key]
        if state == 'changed':
            val1 = stylish(raw_value[('changed', 'from')],
                           replacer, indent_length, depth + 1)
            val2 = stylish(raw_value[('changed', 'to')],
                           replacer, indent_length, depth + 1)
            printable_diff += f'\n{indent}{STATES["deleted"]}{diff_key}: {val1}'
            printable_diff += f'\n{indent}{STATES["added"]}{diff_key}: {val2}'
        else:
            value = stylish(raw_value, replacer, indent_length, depth + 1)
            printable_diff += f'\n{indent}{STATES[state]}{diff_key}: {value}'

    printable_diff += '\n' + indent[:-2] + '}'

    return printable_diff
