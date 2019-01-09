
# codility passed test 0n the 19/09/2019


def grouping_zoo(A):
    count = 0
    for i in range(len(A)):
        try:
            if  A[i+1] > A[i] :
                count += 1
        except IndexError:
            if A[i] > A[i-1]:
                print (A[i])
                count += 1
    return count


lis = [1, 2, 6,5, 10, 9, 8, 11, 12]
li = [5, 4, 3, 2, 6, 1]



# Enforcing that a string contains  a set of characters
def containsOnly(seq, aset):
    """ Check whether sequence seq contains ONLY items in aset. """
    for c in seq:
        if c not in aset: return False
    return True


import re
# Enforcing that a string contains only a set of characters
def contains_only_regex(seq):

    return bool(re.match('^[\[\]({)}]+$', seq))



def format_number_with_commas(num):
    """
     return a comma formatted number
    """

    #error case
    if not isinstance(num, (int, float)):
        return -1 # error

    num_in_string = str(num)

    # list to hold value of the string
    num_in_list = list(num_in_string)

    gap = len(num_in_string)

    # special case
    if type(num) is float:
        indexcomma = num_in_list.index('.')
        gap = len(num_in_string) - (len(num_in_string) - indexcomma)

    while gap > 3:
        index = gap - 3
        num_in_list.insert(index, ',')
        gap -= 3

    return "".join(num_in_list)

print(format_number_with_commas(123003))
print(format_number_with_commas(123003.902))
print(format_number_with_commas('see'))

# a pythonic way of doing it is 

def place_value(number):
    return ("{:,}".format(number))
 
print(place_value(1000000))



def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


# finding all anagrams from a list of words

def find_anagrams(a_list):
    # primes = prime_gen(26)

    primes = []

    for i in range(1, 27):
        primes.append(i)

    # h = OrderedDict()

    h = {}

    for i in range(len(a_list)):
        s = 1
        for j in range(len(a_list[i])):
            word = a_list[i].lower()
            el = word[j]
            index = ord(el) - ord('a')
            s = s*(primes[index])

        g = h.get(s)

        if g == None:
            g = []
        g.append(a_list[i])
        h[s] = g
    
    result = []

    for e in h:
        if len(h[e]) < 2:
            continue
        result.append(h[e])
    return result

# second version

def anagrams(word_list):

    dic = {}
    for word in word_list:
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

print(anagrams(['home', 'meho', 'cool', 'cat', 'tac']))


def check_integers(A):
    if any(not isinstance(y,(int)) for y in A):
        return False
    return True

# print(check_integers([1,3,4]))
# print(check_integers([1,3.4,4]))
# print(check_integers([1,3,4, 'b']))


def place_value(number):
    return ("{:,}".format(number))
 
# print(place_value(1000000))
# print(place_value(1000000.23390))
# print(place_value('sdu'))


# a number is a prime only if it is divisible by itself and 1 except 1:

# example = [2, 3, 5, 7, 11, 13, 17, 19]

import math
def is_prime(N):
    if N <= 2:
        return True
    i = 2
    while i <= math.sqrt(N):
        if N % i == 0:
            return False
        i += 1

    return True

def prime_gen(N):
    result = []
    i = 2
    while len(result) < N:
        if is_prime(i):
            result.append(i)
        i += 1
    return result


def format_word(num):
    st = str(num)

    if len(st) <= 3:
        return st

    length = len(st)
    true_length = length - 3
    first = len(st) % 3

    index_gap = 3

    if first:
        index_gap = first
    

    result = []

    for i in range(length):
        element = st[i] 
        if i == index_gap - 1 and i < true_length:
            result.append(element)
            result.append(',')
            index_gap += 3
        else:
            result.append(element)
    return ''.join(result)


print(format_word(123))
print(format_word(123898))
print(format_word(1238984))

/Users/gasim/.pyenv/shims:/Users/gasim/.pyenv/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin





