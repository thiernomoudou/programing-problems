# Implementing a hash table in python


class Hashtable:
    def __init__(self, hashing_function, size):
        self.size = size
        self.hash_func = hashing_function
        self.table = [[] for i in range(size)]

    def hash(self, key):
        return self.hash_func(key) % self.size
    
    def add(self, key, value):
        self.table[self.hash(key)].append((key,value))
    
    def get(self, key):
        for k, v in self.table[self.hash(key)]:
            if k == key:
                return v
            return None

# we could implement a hash table using a 
# balance binary search tree


# Implement a StringBuilder in python

class StringBuilder:
    def __init__(self, string):
        self.string = string
        self.string_in_list = list(self.string)
    
    def concat(self, word):
        for c in word:
            self.string_in_list.append(c)
        return ''.join(self.string_in_list)


# Implement a linked list in python

# this is the node class
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


# This is the linked list
class LinkedList:

    def __init__(self):
        self.head = None
    
    def __str__(self):
        lk = []
        current = self.head
        while current != None:
            el = current.get_data()
            lk.append(str(el))
            current = current.get_next()
        return ' '.join(lk)


    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count +=1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if item == current.get_data():
                found = True
            current = current.get_next()
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

     def append(self, item):
        current = self.head
        new_node = Node(item)
        if current == None:
            self.head = new_node
        elif current.get_next() == None:
            current.set_next(new_node)
        else:
            while current.next != None:
                current = current.get_next()
            current.set_next(new_node)

    
    def removeDuplicates(self):
        #Write your code here
        current = second = self.head
        while current is not None:
            while second.next is not None:   # check second.next here rather than second
                if second.next.data == current.data:   # check second.next.data, not second.data
                    second.next = second.next.next   # cut second.next out of the list
                else:
                    second = second.next   # put this line in an else, to avoid skipping items
            current = second = current.next
        return self.head

# remove duplicates

def removedup(st):
    l = []
    dic = {}
    i = 0
    while i < len(st):
        if s[i] not in dic:
            e = s[i]
            l.append(e)
            dic[e] = 1
        else:
            i +=1
    return ''.join(l)
        


# Anagragram solution 

def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        print c1[j]
        print 'and'
        print c2[j]
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))
print(anagramSolution4('skji', 'apple'))


# Permuation of Palindrome

# permuation of a palindrome

def removespaces(st):
    li = []
    print (st)
    for i in st:
        if i not in [' ', '\n']:
            li.append(i)
    return ''.join(li)


def permutation_of_palindrome(string):
    st = removespaces(string)
    dic = {}
    for i in st:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    count = 0
    for k in dic:
        if dic[k] % 2 != 0:
            count += 1
    
    if count > 1:
        return False
    return True




# final solution for the two unit test for my toptal firt challenge
def solution (A):
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

print(sol(lis))
print(sol(li))

# Grouping list in order
# toptal example

def is_consecutive(a, b):
    """return True is a and b are
    consecutives and False if not"""
    if a - b == 1:
        return True
    elif a - b == -1:
        return True
    elif a - b == 0:
        return True
    else:
        return False


def in_place_reordering(list):
    """return a new list containing consecutives 
    elements"""
    result = []
    temp = []
    for i in range(1, len(list)):
        if is_consecutive(list[i-1], list[i]):
            temp.append(list[i-1])
        else:
            if temp:
                temp.append(list[i-1])
                result.append(temp)
            else:
                result.append([list[i-1]])
            temp = []
    temp.append(list[-1])
    result.append(temp)
    return result

l1 = [1, 5, 4, 9, 8, 7, 12, 13, 14, 18]
l2 =  [4, 3, 2, 6, 1, 14, 15, 16, 20, 21, 24, 28, 28, 28, 29, 29, 23]
l3 = [1, 2, 3, 8, 9, 6, 7, 11, 10, 14, 15]
l4 = [5, 4, 3, 2, 6, 1]

print l1
print group_elements(l1)
print len(group_elements(l1))

print l2
print group_elements(l2)
print len(group_elements(l2))

print l3
print group_elements(l3)
print len(group_elements(l3))

print l4
print group_elements(l4)
print len(group_elements(l4))


# finding the first non repetive caracter

def fist_non_repeative_character(st):
    """ return the first non reptivtive character
        in a string"""
    # this algo compares any character to each character in the string
    # and has  a big O of (n*n)
    for char in  range (len(st)):
        for ch in range (len(st)):
            if st[ch] == st[char] and char != ch:
                break
        else:
            return st[char]


# Deleting voyels in a string:

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



st = 'hello world'

print(delete_voyels(st))


# reverse words of a string:

def reverse(st):
    # copy it into a list
    # we reverse the words not the caracters
    
    copy_st = st.split()

    # copying words in st_list to new_list backward
    for i in range(len(copy_st)//2):
        temp = copy_st[i]
        copy_st[i] = copy_st[len(copy_st)-1 - i]
        copy_st[len(copy_st)-1 - i] = temp


    return ' '.join(copy_st)



st = 'hello world reversing something'
print (reverse(st))

# converting an integer to it binary representation

ef decimalTobinary(n):
    """return the binary version of n"""

    # Error
    if type(n) is not int:
        return -1

    # edge cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    st = []

    while n > 0:
        remainder = str(n % 2)
        st.append(remainder)
        n //=2
    
    st.reverse()
    
    return ''.join(st)



# implementing my own linked list

# knowing that a linked list is composed on nodes
# let define first a node definition

# node class
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


# linked list

class Linkedlist:
    # constructor like
    def __init__(self):
        self.head = None

    # string representation
    def __str__(self):
        current = self.head
        a_list = []
        if current == None:
            return str(a_list)
        while current != None:
            a_list.append(current.data)
            current = current.next
        return str(a_list)

    def is_empty(self):
        return self.head == None

    # Add elements at the begining of the list
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
    
    # add elements at the end of the list
    def append(self, item):
        current = self.head
        if current == None:
            self.head = item
        while current.next != None:
            current = current.next
        current.next = Node(item)
    
    def search(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            current = current.next
        return False

    # remove v1
    def removev1(self, item):
        current = self.head
        if current.data == item:
            return self.head.next
        while current.next != None:
            if current.next.data == item:
                current.next = current.next.next
                return self.head
            current = current.next
        return self.head

    def removev2(self, item):
        current = self.head
        prev = None
        while current != None:
            if current.data == item:
                if prev:
                    prev.next = current.next
                else:
                    return self.head.next
            prev = current
            current = current.next
        return self.head

    def remove_duplicates(self):
        current = self.head
        prev = None
        a_dict = {}
        while current != None:
            if current.data in a_dict:
                prev.next = current.next
            else:
                a_dict[current.data] = 1
                prev = current
            current = current.next
        return self.head

    # partition the list at a givien item so that elements that are 
    # smaller than item will at the left and those bigger that it at the rieht

    def partition(self, item):
        smaller = self.head
        greater = None
        temp = None

        if self.head == None:
            return False

        current = self.head

        while current != None:
            temp = current.next
            if current.data < item:
                # Append to the tail of smaller
                smaller.next = current
                smaller = current
            else:
                # Add to the head of greater
                current.next = greater
                greater = current
            current = temp

        smaller.next = greater



# sum list  cracking the code
# first part
def add_two(l1, l2):
    if l1 == None and l2 == None:
        return False # Error

    len1 = l1.length()
    len2 = l2.length()
    # pads the sorter lsit with zeros

    if len1 < len2:
        l1 = padlist(l1, len2-len1)
    elif len1 > len2:
        l2 = padlist(l2, len1-len2)
    carry = 0
    result = Linkedlist()
    current1 = l1.head
    current2 = l2.head
    while current1 != None:
        temp = current1.data + current2.data
        el = temp % 10 + carry
        if result == None:
            result.add(el)
        result.append(el)
        if temp >= 10:
            carry = 1
        else:
            carry = 0
        current1 = current1.next
        current2 = current2.next
    
    if carry:
        result.append(carry)

    return result


def padlist(linkedlist, padding):
    for i in range(padding):
        linkedlist.append(0)
    return linkedlist


