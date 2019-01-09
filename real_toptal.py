

# problem 1, score 100%

def solution(ranks):
    # write your code in Python 3.6
    # error case
    
    if not any(isinstance(y, int) for y in ranks) or type(ranks) is not list:
        return 0 # Error case
    
    counter = 0
    current = 1
    
    ranks.sort()
    
    for i in range(1, len(ranks)):
        if ranks[i-1] == ranks[i]:
            current += 1
        if ranks[i] != ranks[i-1] and ranks[i] - ranks[i-1] == 1:
            counter += current
            current = 1
        if ranks[i] != ranks[i-1]:
            current = 1
            
    return counter

# problem 2 , tree problems with score 0


# problem 3, with 57 

def all_proper_prefix(st):
    result = []
    
    for i in range(1, len(st)):
        prefix = st[:i]
        result.append(prefix)
    return result

def all_proper_suffix(st):
    result = []
    for j in range(len(st)-1, 0, -1 ):
        suffix = st[j:]
        result.append(suffix)
    return result
        
# print(allprefix('codility'))
# print(allsuffix('codility'))

def solution3(S):
    if type(S) is not str:
        return -1 # error

    if len(S) == 0:
        return 0

    S = S.lower()

    prefixes = all_proper_prefix(S)

    suffixes = all_proper_suffix(S)

    longest = 0

    for i in range(len(prefixes)):
        pref, suff = prefixes[i], suffixes[i]
        if pref == suff and longest < len(pref):
            longest = len(pref)
    return longest


print(all_proper_prefix('codility'))
print(all_proper_suffix('codility'))
print(solution3('abrab'))

import math
def get_change(M, P):
    # error case

    # our change coins
    changes = [1, 5, 10, 25, 5, 100]

    # result
    result = [0] * (len(changes))

    change = M - P

    if change >= 1:
        integer_part = int(change)
        result[-1] = integer_part
    
    decimal_part = (change*100 - integer_part*100)
    print(decimal_part)

    if decimal_part > 0:
       
        if decimal_part in changes:
            # Find the index of the decimal part to fill our result list
            index = changes.index(decimal_part)
            result[index] += 1
        else:
            tracker = 0
            while decimal_part > 0:
                for i in range(len(changes)-2, -1, -1):
                    element = changes[i]
                    pick = decimal_part - element
                    print(pick)
                    if pick >= 0 and pick in changes:
                        index = changes.index(element)
                        result[index] +=1
                        tracker += element
                decimal_part = decimal_part - element

    return result


print(get_change(5, 0.12))


# Must elegant and simpler version of get change
def change(value, amount):
    # Availabe change
    available_change = [1, 5, 10, 25, 50, 100]

    # Result
    result = [0]* len(available_change)

    change = round((amount - value) * 100)
    # We add hundred to get rid of floating points lack of precision

    # Let fill the result by the number of coins we should give him

    while change > 0:
        for i in range(len(available_change) - 1, -1, -1):
            coin = available_change[i]
            if change >= coin:
                result[i] += 1
                change -= coin
                break
            else:
                continue
    return result

print(change(0.96, 5))
print(change(0.12, 5))

# change v2
def change(value, amount):
    # Availabe change
    available_change = [1, 5, 10, 25, 50, 100]
    # Result
    result = [0]* len(available_change)

    change = (amount - value)
    change = round(change * 100)
    # We add hundred to get rid of floating points lack of precision

    # Let fill the result by the number of coins we should give him
    for i in range(len(available_change)-1, -1, -1):
        coin_value = available_change[i]
        if change >= coin_value:
            number_coin, change = divmod(change,coin_value)
            print(number_coin, change)
            result[i] = number_coin

    return result




