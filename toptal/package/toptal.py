

# def find_word(array):
#     mapper = set()
#     result = []
#     final_result = []
#     for i in range(array):
#         element = array[i]
#         char = element.split()
#         first_char = char[0]
#         second_char = char[1]
#         result.append(first_char)
#         result.append(second_char)

#     for element in result:
#         if element not mapper:
#             final_result.append(element)
#             mapper.add(element)

#     return ''.join(final_result)




def capitalize_string(string):
    result = [string[0].upper()]
    uniformed_string = [string[0]]
    punctuations = ['?', '!', ',', '.']

    for i in range(1, len(string)):
        if string[i] == ' ' and string[i-1] in punctuations:
            continue
        uniformed_string.append(string[i])
    
    for i in range(1, len(uniformed_string)):
        current = uniformed_string[i]
        prev = uniformed_string[i-1]

        if current not in punctuations and prev == '.':
            result.append(' ')
            result.append(current.upper())
        elif current not in punctuations and prev in punctuations \
        and prev != '.':
            result.append(' ')
            result.append(current)
        else:
            result.append(current)
    return ''.join(result)

    
