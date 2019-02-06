
#### list problems


# 1. mergin meeting time
def merge_meetings(mtgs):
    """Return a list of condensed meeting ranges.
    >>> condense_meeting_times([(1, 3), (2, 4)])
    [(1, 4)]
    >>> condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]
    """

    # sort lst so any meetings that can be merged will always be adjacent
    mtgs.sort()

    # initialize merged lst with the earliest meeting
    merged = [mtgs[0]]

    # if the end time of the first meeting overlaps the start time of the second
    # meeting, then merge the two meetings into one time range, which begins at
    # the first meeting's start, and ends at the later of the two end times
    for current_start, current_end in mtgs[1:]:

        # compare to the last meeting we've looked at in the merged lst
        merged_start, merged_end = merged[-1]

        # if the current and last meetings overlap, use the latest end time
        if current_start <= merged_end:
            merged[-1] = (merged_start, max(merged_end, current_end))

        # if the current meeting doesn't overlap, add it to the merged lst
        else:
            merged.append((current_start, current_end))

    return merged

# print(merge_ranges(l))

# Merge meeting v2
def merge_meetings(meetings):
    meetings.sort()
    previous = list(meetings[0])
    result = []
    for i in range(1, len(meetings)):
        meeting = meetings[i]
        if meeting[0] <= previous[1]:
            previous[1] = max(meeting)
        else:
            result.append(tuple(previous))
            previous = list(meeting)
    result.append(tuple(previous))
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

# reverse word list not in place
def reverse_words_v2(array):

    result = []
    word = []
    for i in range (len(array)):
        word.append(array[i])
        if i + 1 == len(array) or array[i] == ' ':
            string = ''.join(word)
            result.append(string.strip())
            word  =  []
    result.reverse()
    return ' '.join(result)
# 4. merging sorted list

# print(mergelist([1, 3, 5], [2, 4]))
def mergelistv2(list1, list2):
    # length = len(list1) if len(list1) >= len(list1) else: len(list2)
    
    n1, n2 = len(list1), len(list2)

    result = [None] * (n1 + n2)
    
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


# Reverse word in place 
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

# Reverse word not in place
def reverse_words_not_inplace(phrase):
    result = []
    word = []
    for i in range(len(phrase)-1, -2, -1):
        char = phrase[i]
        if i == -1 or char == ' ':
            word.reverse()
            final_word = ''.join(word).strip()
            result.append(final_word)
            word = []
        word.append(char)
    return ' '.join(result)

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

# message = 'cake, pound, steal'
print(message)
print(reverse_words_not_inplace(message))

# counting words
# Inflight entertainement

def flight_entertain(flight_length, movies_length):
    """return whether there are 2 movies
    whose sum is equal to the fligh length"""
    if type(flight_length) is not int:
        return -1 # Error case

    movie_table = {}
    # Throw all elements of the movies list to the table
    # for easy finding
     for i in range(len(movies)):
            movie_length = nums[i]
            if flight_length-movie_length in movie_table:
                return True
            movie_table[movie_length] = i
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
        if len(dups[0]) > 1:
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

def rotation_point(array):
    first_word = array[0]
    floor = -1
    ceiling = len(array)

    while floor + 1 < ceiling:
        distance = ceiling - floor
        half_distance = distance // 2

        guess_index = floor + half_distance

        if array[guess_index] > first_word:
            floor = guess_index
        else:
            ceiling =guess_index

        # if floor + 1 == ceiling:
        #     break

    return ceiling

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

# Duplicate optimize for space
def find_duplicate(array):
    n = len(array)
    for i in range(n):
        if(arr[abs(arr[i])] > 0) : 
            print(arr[abs(arr[i])])
            arr[abs(arr[i])] = (-1) * arr[abs(arr[i])] 
        else :
            return abs(arr[i])

    return None

arr = [1, 2, 3, 4, 5, 1, 1]
print(arr)
print(find_duplicate(arr))

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

# another find duplicate using linked list
def find_duplicate(list):
    """find a duplicate of 1..n in a list n+1 elements long"""

    n = len(list)
    i = n
    j = n
    while True:
        print("looking for cycle: i %s j %s" % (i, j))
        i = list[i - 1]  # tortoise
        j = list[j - 1]  # hare
        if i == j:
            print("cycle found at %s" % i)
            break

    # we found a cycle
    # now restart j
    # and loop until j meets i again
    # and that's the start of the cycle (or the dup)

    j = n
    while True:
        print("looking for dup: i %s j %s" % (i, j))
        i = list[i - 1]
        j = list[j - 1]
        if i == j:
            print("dup found at %s" % i)
            break

    print("dup is %s" % i)
    return i

l = [2,2, 1, 3]
find_duplicate(l)



# recursion 
# Permute string
result = set()
def permute(string, step=0):
    if step == len(string):
        result.add(''.join(string))
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

# thieft cake
def max_duffle_bag_value1(cake_tuples, capacity):

    while (0,0) in cake_tuples:
        cake_tuples.pop(cake_tuples.index((0,0)))

    try:
        price_per_pound = [(cake[1]//cake[0], cake[1], cake[0]) for cake in cake_tuples]
    except ZeroDivisionError:
        #return sys.maxint
        return "Infinite"
    bag_value = 0

    while len(price_per_pound) > 0:
        most_valueable_cake = max(price_per_pound)
        print (most_valueable_cake)
        bag_value += capacity//most_valueable_cake[2]*most_valueable_cake[1]
        capacity %= most_valueable_cake[2]
        print (capacity)
        price_per_pound.pop(price_per_pound.index(most_valueable_cake))

    return bag_value
    
print (max_duffle_bag_value1(ct, cap))


#  parenthese math
def parenthese_matching(string, index=0):
    number_of_parenthes = 0

    for i in range(index, len(string)):
        char = string[i]
        if char == '(':
            number_of_parenthes += 1
        if char == ')':
            number_of_parenthes -= 1
            if number_of_parenthes == 0:
                return i
    return -1 # error


# bracket validator
def bracket_validator(string):
    openers = []
    brackets = { '(': ')', '[': ']', '{':'}' }
    for i in range(len(string)):
        char = string[i]
        if char in '({[':
            openers.append(char)
        if char in ')}]':
            if not openers:
                return False
            else:
                last_opener = openers.pop()
                if brackets[last_opener] != char:
                    return False

    return len(openers) == 0

st = '(((({home))))'
print(bracket_validator(st))


# max stack
class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):
    def __init__(self):
        super().__init__()
        self.max_tracker = Stack()
        self.max_element = float('-inf')

    def get_max_element(self):
        return self.max_tracker.peek()

    def push(self, item):
        if item > self.max_element:
            self.max_tracker.push(item)
            self.max_element = item
        super().push(item)

    def pop(self):
        if super().peek() == self.max_tracker.peek():
            self.max_tracker.pop()
        super().pop()


# Triangular series

# which appears twice
def which_appears_twice(array):
    n = len(array)

    partial = (n*(n-1))//2
    total = sum(array)
    return total - partial


arr = [1, 2, 3, 4, 3]

print(which_appears_twice(arr))

# simulate_5_sided_die 
# knowing that your rand7()

def rand5():
    roll = rand7()
    return roll if roll <= 5 else rand5()



# Reverse a linked list
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to reverse the linked list 
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam'    : ['Nathan', 'Jayden', 'William'],
    'Omar'    : ['Ren', 'Min', 'Scott'],
}

print(find_shortes_path(network, 'Jayden', 'Adam'))

