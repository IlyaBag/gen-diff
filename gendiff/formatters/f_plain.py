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


def plain(diff, key_path_global=[]):  # noqa: C901
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
            continue
        path = '.'.join(key_path)
        if state == 'deleted':
            line = f"Property '{path}' was removed"
            printable_diff.append(line)
            continue
        if state == 'added':
            value = fix_syntax(value)
            line = f"Property '{path}' was added with value: {value}"
            printable_diff.append(line)
            continue
        if state == 'changed':
            val1 = fix_syntax(value[('changed', 'from')])
            val2 = fix_syntax(value[('changed', 'to')])
            line = f"Property '{path}' was updated. From {val1} to {val2}"
            printable_diff.append(line)
    return '\n'.join(printable_diff)
