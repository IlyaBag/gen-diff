STATES = {'deleted': '-',
          'added': '+',
          'same': ' ',
          'changed': '',  # здесь должа быть функция??
          'nested': ' '}


def stylish(data, replacer=' ', indent_length=4) -> str:
    if not isinstance(data, dict):
        return get_printable_value(data)  # переводим значение в строку
    
    keys = list(data.keys())
    keys.sort()

    printable_diff = '{'

    for key in keys:
        state, value = data[key]
        nested_value = stylish(value, replacer, indent_length)
        
        # f'{state_char} {key}: {value}'

    printable_diff += '\n}'

    return printable_diff
