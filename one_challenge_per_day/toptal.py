

# ['p>e', 'e>r', 'r>u'] >> peru


def recombine(array):
    result = []
    mapper = set()
    finalresult = []
    for i in range(len(array)):
        char = array[i].split('>')
        first = char[0]
        second = char[1]
        result.append(first)
        result.append(second)

    for char in result:
        if char not in mapper:
            finalresult.append(char)
            mapper.add(char)
        

    return ''.join(finalresult)

arr = ['p>e', 'e>r', 'r>u']

print(recombine(arr))



# 'this is something...that,is good.and do I know?what.'

def correctPhrase(string):
    result = []
    punctuations = ['.', '?', '!', ',']

    for char in string:
        result.append(char)
        if char in punctuations:
            result.append(' ')

    return ''.join(result)



