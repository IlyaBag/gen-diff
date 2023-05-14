STATES = {'deleted': '- ',
          'added': '+ ',
          'same': '  ',
          'changed_from': '- ',  # здесь должа быть функция??
          'changed_to': '+ ',  # здесь должа быть функция??
          'nested': '  '}


def stylish(data, replacer=' ', indent_length=4) -> str:
    if not isinstance(data, dict):
        return str(data)  # get_printable_value(data)  # переводим значение в строку
    
    keys = list(data.keys())
    keys.sort()

    printable_diff = '{'

    indent = replacer * (indent_length - 2)
    for key in keys:
        diff_key, state = key
        raw_value = data[key]
        value = stylish(raw_value, replacer, indent_length)
        printable_diff += f'\n{indent}{STATES[state]}{diff_key}: {value}'

    printable_diff += '\n}'

    return printable_diff

from tests.fixtures.mein_raw_diff_flat import diff

print(stylish(diff))