def fix_syntax(string):
    if string in ('True', 'False'):
        return string.lower()
    return string


def show_diff(diff):
    printable_diff = '{'
    for pair in diff:
        printable_diff += f'\n  {pair[0]}: {fix_syntax(pair[1])}'
    printable_diff += '\n}'
    return printable_diff
