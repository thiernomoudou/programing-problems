

def correctPhrase(string):
    result = []
    punctuations = ['?', '!', ',']

    result.append(string[0].upper())
    for i in range(1, len(string)):
        char = string[i]
        if char in punctuations:
            result.append(char)
            result.append(' ')
        elif char != '.' and string[i-1] == '.':
            result.append(' ')
            result.append(char.upper())
        else:
            result.append(char)


    return ''.join(result)



st = 'this is something...that,is good.and do I know?what.'

print(correctPhrase(st))


