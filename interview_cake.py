
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

# permuation of palindrome

def perm_palindrom(string):

    if len(string) % 2 == 0:
        return False

    # Assuming ASCII
    counter = [0] * 128
    for char in string:
        ordinal = ord(char)
        counter[ordinal] += 1
    unique = 0
    for count in counter:
        # If we found a second count that is equal to 1
        if unique and count % 2 != 0:
            return False
        if count == 1:
            unique += 1
    return True


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

# word counte v2
def word_counter(string):
    word_list = string.split()
    new_list = []
    for word in word_list:
        new_word = word.strip('.:-/').lower()
        new_list.append(new_word)
    counter = {}
    for element in new_list:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1
    return counter

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


# Find duplicate files
import os, sys
import hashlib

def find_duplicates(parentFolder):
    # duplicate in format {hash:[names]}
    
    if not os.path.exists(parentFolder):
        return '{} is not a valid path, please verify'.format(parentFolder)

    dups = {}
    # Duplicate list
    duplicate_list = []
    for dirName, subdirs, filelist in os.walk(parentFolder):
        print('Scanning {}'.format(dirName))
        for filename in filelist:
            # Pick the path of the file
            path = os.path.join(dirName, filename)
            # Getting the last time the inode change
            date = os.path.getctime(path)
            # Determine the hash
            file_hash = hash_file(path)
            # Add the file path to the duplicate dictionnary
            if file_hash in dups:
                dups[file_hash].append((path, date))
            else:
                dups[file_hash] = [(path, date)]

    for key in dups:
        if len(dups[key]) > 1:
            # Sort the list by creation date to always get the original file
            # at the end of the list
            value = sorted(dups[key], key=lambda l: l[1], reverse=True)
            tup = []
            for element in value:
                tup.append(element[0])
            duplicate_list.append(tuple(tup))

    return duplicate_list


def hash_file(path, blocksize=65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buff = afile.read(blocksize)
    while len(buff) > 0:
        hasher.update(buff)
        buff = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

path='dup'
print(find_duplicates(path))


# Greedy algorithm

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

# Highest product of three

# Highest product of three

def highest_product_three(integers):
    if len(integers) < 3:
        return -1 # Error case
     
    # sort the list to order integers
    extreme_left = integers[0] * integers[1] * integers[2]
    extreme_right = integers[-1] * integers[-2] * integers[-3]

    result = max(extreme_right, extreme_left)

    return result

integ = [1, 5, 3, 4]

print(highest_product_three(integ))


# Product of others

def product_of_others(integers):
    result = [0]*len(integers)

    for i in range(len(result)):
        result[i] = product(i, integers)
    return result

def product(index, array):
    product = 1
    for j in range(len(array)):
        num = array[j]
        if j != index:
            product *= num
    return product

arr = [1, 7, 3, 4]

print(product_of_others(arr))

# Shuffle list elements
import random

def suffle_elements(array):
    # In place list suffle
    for i in range(len(array)-1, -1, -1):
        
        # Pick a random index from 0 to i
        j = random.randint(0, i+1)

        array[j], array[i] = array[i], array[j]

    return array

arr = [1, 7, 3, 4]
print(arr)
print(suffle_elements(arr))

# search and sorting algorithm

# Counting sort
def counting_sort(the_list, max_value):
    
    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input
    # etc.
    counts = [0] * (max_value + 1)
    for item in the_list:
        counts[item] += 1

    # Initialize the indices list based on the number of 
    # items in the input that are smaller.
    # indices[0] stores the index in the sorted list where the next 0 goes
    # indices[4] stores the index in the sorted list where the next 4 goes
    indices = []
    num_items_before = 0
    for count in counts:
        indices.append(num_items_before)
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(the_list)

    # Run through the input list,
    for item in the_list:
        
        # Place the item in the sorted list
        sorted_list[ indices[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        indices[item] += 1

    return sorted_list

# Rotation point
def rotation_point(arr):
    lowest_index = 0
    highest_index = len(arr) - 1

    while lowest_index + 1 < highest_index:
        distance = lowest_index + highest_index
        half_distance = distance // 2
        guess_index = half_distance
        guess = arr[guess_index]
        if guess > arr[guess_index + 1]:
            return guess_index + 1
        if guess < arr[guess_index - 1]:
            return guess_index

        if guess < arr[highest_index]:
            highest_index = guess_index
        else:
            lowest_index = guess_index
    return -1

# Repeated integer
def repeat_int(arr):
    n = len(arr) + 1
    counter = [0] * n

    for element in arr:
        counter[element] += 1

    for i in range(len(counter)):
        element = counter[i]
        if element > 1:
            return i
    return 0

# Duplicate int optimized for space
# repeat int v2
def duplicate_int(integers):
    """find the number in ints that appears twice"""

    n = len(integers)
    # n ints, so the list is
    # 1..(n-1) + some duplicated number
    # = ((n-1) * (1 + n - 1) / 2)
    # = ((n-1) * (n) / 2)
    # = ((n-1) * (n / 2.0)
    gauss = (n * (n - 1 )) // 2
    total = sum(integers)
    duplicate = total - gauss
    return duplicate

arr = [1, 2, 2, 3, 4]
print(duplicate_int(arr))










# recursion 
# Permute string
result = set()
def permute(string, step=0):
    if step == len(string):
        result.add(''.join(string))
    else:
        for i in range(step, len(string)):
            string = list(string)
            string[step], string[i] = string[i], string[step]
            permute(string, step + 1)
    return result

# print(permute('abc'))

class Permute:
    def __init__(self):
        self.result = set()

    def permute(self, string, step=0):
        if step == len(string):
            self.result.add(''.join(string))
        for i in range(step, len(string)):
            string = list(string)
            string[step], string[i] = string[i], string[step]
            self.permute(string, step + 1)
        return self.result


print(Permute().permute('abc'))

# make change

def change(amount, denominations):
    # below: the index is the amount and the value
    # at each index is the number of ways
    # of getting that amount

    # initialize an array of zeros with indices
    # up to amount
    arrangement = [0] * (amount + 1)

    arrangement[0] = 1

    for coin in denominations:
        higher_amount = coin
        while higher_amount <= amount:
            remainder = higher_amount - coin
            arrangement[higher_amount] += arrangement[remainder]
            higher_amount += 1
    return arrangement[amount]


amount = 4
denominations = [1,2,3]

print(change(amount, denominations))

def make_change(amount, denominations):
    # print "Amount :", amount, " Denominations:", denominations
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 0:
        return 0
    return make_change(amount-denominations[0], denominations) + \
        make_change(amount, denominations[1:])

print(make_change(amount, denominations))