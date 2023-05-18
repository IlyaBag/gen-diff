# STATES = {'deleted': '- ',
#           'added': '+ ',
#           'same': '  ',
#           'changed_from': '- ',
#           'changed_to': '+ ',
#           'nesting': '  ',
#           'nested': '  '}


def fix_syntax(item):
    if isinstance(item, dict):
        return '[complex value]'
    if isinstance(item, bool):
        return str(item).lower()
    if isinstance(item, int):
        return item
    if item is None:
        return 'null'
    return f"'{item}'"


# def is_leaf_node(item):
#     if '_state_' in item and '_value_' in item:
#         return True
#     return False


def plain(diff, key_path_global=[]):
    printable_diff = []
    keys = list(diff.keys())
    keys.sort()
    for diff_key in keys:
        key, state = diff_key
        if state == 'same':
            continue
        key_path = key_path_global[:]
        key_path.append(key)
        value = diff[diff_key]
        if state == 'nesting':
            nested_diff = plain(value, key_path)
            printable_diff.append(nested_diff)
        else:
            # val1 = value.get('_value_')
            # if isinstance(val1, dict):
            #     val1 = '[complex value]'
            # else:
            #     val1 = fix_syntax(val1)
            # val2 = value.get('_value2_', '')
            # if isinstance(val2, dict):
            #     val2 = '[complex value]'
            # else:
            #     val2 = fix_syntax(val2)
            path = '.'.join(key_path)
            if state == 'changed':
                value1 = fix_syntax(value[0])
                value2 = fix_syntax(value[1])
                diff_line = f"Property '{path}' was updated. From {value1} to {value2}"
                printable_diff.append(diff_line)
            else:
                value = fix_syntax(value)
                layouts = {
                    "deleted": f"Property '{path}' was removed",
                    "added": f"Property '{path}' was added with value: {value}",
                    # "changed": f"Property '{path}' was updated. From {value1} to {value2}"
                }
                diff_line = layouts[state]
                printable_diff.append(diff_line)
    return '\n'.join(printable_diff)
