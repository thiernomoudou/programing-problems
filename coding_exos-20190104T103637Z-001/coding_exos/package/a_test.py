def perm(st1, st2):
    if not isinstance(st1, str) or not isinstance(st2, str):
        return -1 # error cases
    
    # special cases
    if len(st1) != len(st2):
        return False

    counters = [0]*128

    for element in st1:
        num_element = ord(element)
        counters[num_element] += 1

    for element in st2:
        num_element = ord(element)
        counters[num_element] -=1
        if counters[num_element] < 0:
            return False
    return True 


def anagrams(word_list):

    dic = {}
    for word in word_list:
        word = word.lower().strip()
        num_word = 0
        for char in word:
            num_char = ord(char)
            num_word += num_char


        word_value = dic.get(num_word, [])

        word_value.append(word)
        dic[num_word] = word_value

    result = []

    for element in dic:
        value = dic[element]
        if len(value) < 2:
            continue
        result.append(value)

    return result


def binarygap(num):
    
    # error case
    if not isinstance(num, int):
        return -1

    current_gap = 0
    max_gap = 0

    # handling trailing zeros
    while num > 0 and num % 2 == 0:
        num //= 2

    while num > 0:
        reminder = num % 2
        if reminder == 0:
            current_gap += 1
        if reminder == 1 and current_gap:
            max_gap = max(current_gap, max_gap)
            current_gap = 0
        num //= 2

    return max_gap










