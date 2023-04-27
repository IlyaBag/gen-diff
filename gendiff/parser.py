def fix_syntax(string):
    if string in ('True', 'False'):
        return ' ' + string.lower()
    if string == 'None':
        return ' null'
    if string == '':
        return ''
    return ' ' + string


def show_diff(diff, replacer=' ', indent_length=4):
    def inner(cur_diff, accum_indent):
        cur_indent_length = accum_indent + indent_length
        cur_indent = replacer * (cur_indent_length - 2)
        printable_diff = '{'
        for key in cur_diff:
            if isinstance(cur_diff[key], dict):
                # может отдельную функцию для словарей?
                printable_diff += f'\n{cur_indent}{key}: {inner(cur_diff[key], cur_indent_length)}'
            else:
                printable_diff += f'\n{cur_indent}{key}:{fix_syntax(cur_diff[key])}'
        printable_diff += '\n' + replacer * accum_indent + '}'
        return printable_diff
        return inner(diff, 0)
    # printable_diff = '{'
    # for pair in diff:
    #     printable_diff += f'\n  {pair[0]}: {fix_syntax(pair[1])}'
    # printable_diff += '\n}'
    # return printable_diff
