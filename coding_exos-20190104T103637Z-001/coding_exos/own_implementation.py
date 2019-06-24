

def is_anagram(st1, st2):
    if len(st1) != len(st2):
        return False
    letters = [0]*128 # assuming ascii

    for char in st1:
        index = ord(char)
        letters[index] += 1

    for ch in st2:
        index = ord(ch)
        letters[index] -=1

        if letters[index] < 0:
            return False
    return True


def prime_gen(N):
    primes = []
    start = 2
    while len(primes) < N:
        if is_prime(start):
            primes.append(start)

        start += 1
    return primes

import math
def is_prime(n):
    """Return if a given number n is a prime or not"""
    if n <=  2:
        return True
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True 


from collections import OrderedDict
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

    # for e in h:
    #     print(h[e])

# word = ["eat", "pots", "onset", "stone", "rail", "risen", "caret", "resin", 
#     "react", "siren", "sitar", "stair", "liar", "stop", "trace", "notes", "tea", "lair"]

word = ['eat', 'home', 'green', 'tea', 'yellow', 'meho']
# find_anagrams(word)
print (find_anagrams(word))

def binary_search(a_list, target):
    # let build extreme side of the the side

    left = -1
    right = len(a_list)

    while left + 1 < right:

        distance = right - left

        middle = distance // 2

        guess_index = left + middle

        guess_element = a_list[guess_index]


        if guess_element == target:
            return True
        elif guess_element > target:
            right = guess_element
        else:
            left = guess_element
    return False





