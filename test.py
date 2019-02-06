

def delete_voyels(st):
    if type(st) is not str :
        raise ValueErro('Arguments should be strings')
    dic = {}
    # creating a dictionnary containing lowercase and uppercase voyels
    for voyel in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        dic[voyel] = 1

    # copying the string into a list for mutability
    # copy_string = []
    # for char in st:
    #     copy_string.append(char)
    
    copy_string = []

    # Deleting voyels
    for index in range (len(st)):
        character = st[index]
        if character in dic:
            continue
        copy_string.append(character)

    # returnin a new string:
    return ''.join(copy_string)


def delete_voy(st):
    result = []
    voyels = ['a', 'e', 'i', 'o', 'u']

    for char in st:
        if char not in voyels:
            result.append(char)
    return ''.join(result)

st = 'hello world'

print(delete_voy(st))
