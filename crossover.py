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

print(column_name(1))

