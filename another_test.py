
def formatCurr(integer):
    st = str(integer)
    result = list(st[0])
    for i in range(1, len(st)):
        if (len(st) - i) % 3 == 0:
            result.append(',') 
        result.append(st[i])
    return ''.join(result)

def gen_format_curren(any_number):
    result = []
    negative_part = ''
    decimal_part = ''
    # check if the number is negative
    if any_number < 0:
        negative_part = '-'
    number_string=str(any_number).strip('-');
    # check if the number is a floating point
    if isinstance(any_number, float):

        splitted = number_string.split('.')
        number_string = splitted[0]
        decimal_part = splitted[1]
    formatted = formatCurr(number_string);
    result.append(negative_part)
    result.append(formatted)
    if decimal_part:
        result.append('.')
    result.append(decimal_part)

    return ''.join(result)


print(gen_format_curren(-13008.098766))