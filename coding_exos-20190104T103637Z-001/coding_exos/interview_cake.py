
#### list problems


# 1. mergin meeting time

def merge_meeting(array):
    result = []
    array.sort()
    previous = list(array[0])
    for i in range(1, len(array)):
        meeting = array[i]
        if meeting[0] > previous[1] or i == len(array)-1:
            result.append(tuple(previous))
            previous = list(meeting)
        else:
            previous[1] = max(meeting)
        
    return result
# l =[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] return [(0, 1), (3, 8), (9, 12)]

# l =[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# print(merge_ranges(l))

# Merge meeting v2
def merge_meeting(meetings):
    meetings.sort()
    previous = list(meetings[0])
    result = []


    for i in range(1, len(meetings)):
        meeting = meetings[i]
        if meeting[0] <= previous[1]:
            previous[1] = max(meeting)
        else:
            result.append(previous)
            previous = list(meeting)
    result.append(previous)
    return result

l =[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

print(merge_meeting(l))


# 2. reversing a list in place

def in_place_reverse(st):
    st = list(st)

    half_list = len(st) // 2

    for i in range(half_list):
        # create temp variable 
        temp = st[i]
        end = len(st) - i - 1

        # reverse
        st[i] = st[end]
        st[end] = temp

    return ''.join(st)

# print(in_place_reverse('home'))


# 3. Reverse words

def reverse_words(array):
    # reverse the whole array
    array.reverse()

    current_index = 0
    for i in range(len(array) + 1):
        if i == len(array) or array[i] == ' ':
            reverse_characters(array, current_index, i-1)
            current_index = i + 1

    return ''.join(array)


def reverse_characters(word_array, start_index, end_index):
    while start_index < end_index:
        temp = word_array[start_index]
        word_array[start_index] = word_array[end_index]
        word_array[end_index] = temp
        start_index += 1
        end_index -= 1


message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

# print(reverse_words(message))


# 4. merging sorted list

def mergelist(list1, list2):
    list1.extend(list2)
    list1.sort()

    return list1

# print(mergelist([1, 3, 5], [2, 4]))
def mergelistv2(list1, list2):
    # length = len(list1) if len(list1) >= len(list1) else: len(list2)
    
    n1, n2 = len(list1), len(list2)

    result = [None]* (n1 + n2)
    
    # initialize trackers, i will track list1, j list2 and k track result 
    i, j, k = 0, 0, 0

    while i < n1 and j < n2:
        # pick the smallest element correspondent to current position between the 
        # two lists and append them to the result list
        current_list1, current_list2 = list1[i], list2[j]
        if current_list1 < current_list2:
            result[k] = current_list1
            i += 1
            k += 1
        else:
            result[k] = current_list2
            j += 1
            k += 1

    while i < n1:
        result[k] = list1[i]
        i += 1
        k += 1

    while j < n2:
        result[k] = list2[j]
        j += 1
        k += 1

    return result

list1 = [1, 3, 5, 6, 8, 10]
list2 = [2, 4, 7,11 ]

print(mergelistv2(list1, list2))


# Reverse word
def reverse_words(array):
    # reverse the whole array
    array.reverse()

    current_index = 0

    for i in range(len(array) + 1):
        if i == len(array) or array[i] == ' ':
            reverse_characters(array, current_index, i-1)
            current_index = i + 1

    return ''.join(array)


def reverse_characters(word_array, start_index, end_index):
    while start_index < end_index:
        temp = word_array[start_index]
        word_array[start_index] = word_array[end_index]
        word_array[end_index] = temp
        start_index += 1
        end_index -= 1


message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

print(reverse_words(message))


#  Interview cake

# Apple stock price

def get_max_profit(stock_price):
    # Knowing we have to buy before selling
    # and the stock price is chronological
    # we need to get at least two entries in the
    # stock price list
    if len(stock_price) < 2:
        return 'stock price list should get at least two entries'
    
    # Starting price for yesterday being the first element of the list
    # We can consider that is the initial value or the lowest value

    lowest_value = stock_price[0]
    max_profit = stock_price[1] - stock_price[0]

    for i in range (len(stock_price)):
        current_stock_value = stock_price[i]

        current_profit = current_stock_value - lowest_value
        max_profit = max(max_profit, current_profit)
        lowest_value = min(current_stock_value, lowest_value)

    return max_profit

stock_prices = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices))




# counting words
# Inflight entertainement

def flight_entertain(flight_length, movies):
    """return whether there are 2 movies
    whose sum is equal to the fligh length"""

    if type(flight_length) is not int:
        return -1 # Error case

    table = {}

    # Throw all elements of the movies list to the table
    # for easy finding

    for movie in movies:
        table[movie] = True
    
    for movie in movies:
        diff = flight_length - movie
        if diff in table:
            return True
    return False


movies1 = [3, 10, 13, 15, ]
movies2 = [10, 15, 13, 15, 25, ]
print(flight_entertain(50, movies1))
print(flight_entertain(40, movies2))



# counting words
# Word cloud

def word_counter(text):
    wordlist = split_and_lower(text)
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))


def split_and_lower(phrase):
    result = []
    start = 0
    for i in range(len(phrase) + 1):
        if i == len(phrase) or phrase[i] == ' ':
            word = []
            for j in range(start, i):
                word.append(phrase[j])
            word_string = ''.join(word)
            start = i + 1
            # removing punctuations
            result.append(word_string.lower().strip('.,:/'))
    return result


       
text = 'After beating the eggs, Dana read the next step:'

print(word_counter(text))

# Top scores

import time
import random
# top scores
# sorted_scores

def builtin_sort(unsorted_scores, highest_possible_score):
    result = sorted(unsorted_scores, reverse=True)
    return result

def sort_scores_v2(unsorted_scores, max_score):
    result = [0]*(max_score + 1)

    for i in range(len(unsorted_scores)):
        # checking the diffence between max and current score
        diff = max_score - unsorted_scores[i]

        # The difference the max and the highest scores being the
        # smallest diffence, we can get a list of a descending
        # sorted list by assigning the current score the diff index
        # of the result list
        result[diff] = unsorted_scores[i]

    # Filter the list and skip repetitive scores
    filtered = list(filter(lambda score: score, result))
    return filtered

def filter_array(array):
    new_array = []
    for i in range(len(array)):
        if array[i]:
            new_array.append(array[i])
    return new_array

def sort_scores(unsorted_scores, highest_possible_score):

    if type(highest_possible_score) is not int:
        return -1 # Error case

    # creating a list of all number from to highest_possible_score
    counter = [0] * (highest_possible_score + 1)

    # Marking elements that belong to the unsorted_scores list
    for unsorted_score in unsorted_scores:
        counter[unsorted_score] += 1

    sorted_scores = []

    for i in range(len(counter)-1, -1, -1): # Descending
        score_count = counter[i]

        if score_count:
            for j in range(score_count):
                sorted_scores.append(i)

    return sorted_scores


# unsorted_scores = [37, 89, 41, 65, 91, 53, 89, 65, 65]
unsorted_scores = random.sample(range(100), 100)
HIGHEST_POSSIBLE_SCORE = 100

start1 = time.time()
print(builtin_sort(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
end1 = time.time()

t1 = end1-start1
print(t1)

start2 = time.time()
print(sort_scores_v2(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
end2 = time.time()

t2 = end2-start2
print(t2)

print('is it true that sort_scores is faster that the builtin one', t1 > t2)

# Top scores
def sort_scores_v2(unsorted_scores, max_score):
    result = [0]*(max_score + 1)

    for i in range(len(unsorted_scores)):
        # checking the diffence between max and current score
        diff = max_score - unsorted_scores[i]

        # The difference the max and the highest scores being the
        # smallest diffence, we can get a list of a descending
        # sorted list by assigning the current score the diff index
        # of the result list
        result[diff] = unsorted_scores[i]

    # Filter the list and skip repetitive scores
    filtered = list(filter(lambda score: score, result))
    return filtered
