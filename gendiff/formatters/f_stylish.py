import gendiff.diff_states as s


STATES = {s.DELETED: '- ',
          s.ADDED: '+ ',
          s.SAME: '  ',
          s.NESTING: '  ',
          s.NESTED: '  '}


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
        if state == s.CHANGED:
            val1 = stylish(raw_value[s.CHANGED_FROM],
                           replacer, indent_length, depth + 1)
            val2 = stylish(raw_value[s.CHANGED_TO],
                           replacer, indent_length, depth + 1)
            printable_diff += f'\n{indent}{STATES[s.DELETED]}{diff_key}: {val1}'
            printable_diff += f'\n{indent}{STATES[s.ADDED]}{diff_key}: {val2}'
        else:
            value = stylish(raw_value, replacer, indent_length, depth + 1)
            printable_diff += f'\n{indent}{STATES[state]}{diff_key}: {value}'

    printable_diff += f'\n{indent[:-2]}{"}"}'

    return printable_diff
