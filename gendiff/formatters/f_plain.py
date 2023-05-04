def fix_syntax(string):
    if string in ('True', 'False'):
        return string.lower()
    if string == 'None':
        return 'null'
    return f"'{string}'"


def is_leaf_node(item):
    if '_state_' in item and '_value_' in item:
        return True
    return False


def plain(diff, key_path_global=[]):
    printable_diff = []
    keys = list(diff.keys())
    keys.sort()
    for key in keys:
        key_path = key_path_global[:]
        key_path.append(key)
        value = diff[key]
        if is_leaf_node(value):
            state_sign = value.get('_state_') + value.get('_state2_', '')
            if state_sign == ' ':
                continue
            val1 = value.get('_value_')
            if isinstance(val1, dict):
                val1 = '[complex value]'
            else:
                val1 = fix_syntax(str(val1))
            val2 = value.get('_value2_', '')
            if isinstance(val2, dict):
                val2 = '[complex value]'
            else:
                val2 = fix_syntax(str(val2))

            states = {
                "-": "removed",
                "+": f"added with value: {val1}",
                "-+": f"updated. From {val1} to {val2}"
            }

            state = states[state_sign]
            path = '.'.join(key_path)
            diff_line = f"Property '{path}' was {state}"
            printable_diff.append(diff_line)
        else:
            nested_diff = plain(value, key_path)
            printable_diff.append(nested_diff)
    return '\n'.join(printable_diff)
