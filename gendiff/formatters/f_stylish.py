STATES = {'deleted': '- ',
          'added': '+ ',
          'same': '  ',
          'changed_from': '- ',
          'changed_to': '+ ',
          'nesting': '  '}


def stylish(data, replacer=' ', indent_length=4, depth=1) -> str:
    if not isinstance(data, dict):
        return str(data)  # get_printable_value(data)  # переводим значение в строку

    indent = replacer * (indent_length * depth - 2)

    printable_diff = indent[:-2] + '{'
    
    keys = list(data.keys())
    keys.sort()

    for key in keys:
        diff_key, state = key
        raw_value = data[key]
        value = stylish(raw_value, replacer, indent_length, depth + 1)
        printable_diff += f'\n{indent}{STATES[state]}{diff_key}: {value}'

    printable_diff += indent[:-2] + '\n}'

    return printable_diff



from tests.fixtures.mein_raw_diff_flat import diff

print(stylish(diff))