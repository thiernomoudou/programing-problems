def column_name(n):
    if n < 0:
        return -1
    result = []
    alphabets =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(n):
        index = i // 26
        item = []
        if index > 0:
            item.append(alphabets[index-1])
        item.append(alphabets[i % 26])
        result.append(''.join(item))
    return result


# print(column_name(27))
# print(column_name(28))

def get_colum_letter(col_id):
    # include all allowed columns
    if not 1 <= col_id <= 18278:
        raise valueError('Invalid colums index {0}'.format(col_id))
    letters = []
    while col_id > 0:
        col_id, remainder = divmod(col_id, 26)
        if remainder == 0:
            remainder = 26
            col_id -= 1
        letters.append(chr(remainder + 64))
    return ''.join(reversed(letters))

print(get_colum_letter(2))
print(get_colum_letter(3))
print(get_colum_letter(35))


