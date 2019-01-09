# nth fib with bottom up memoization 
def fibo(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(2, n):
        c = a + b
        a, b = b, c

    return a + b


# nth fibonacci number with memoization in python

def fib(n):
    def fib_memo(n, m):
        """
        Find the n'th fibonacci number. Uses memoization.

        :param n: the n'th fibonacci number to find
        :param m: dictionary used to store previous numbers
        :return: the value of the n'th fibonacci number
        """

        if n in m:
            return m[n]

        answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
        m[n] = answer
        return answer

    m = {1: 1, 2: 1}
    return fib_memo(n, m)







# exos on stacks

import sys
# Stack

class Stack:
    """implement a stack data type with push, pop , peek and 
        others methods using python list data type"""

    def __init__(self): 
        self.stack = [] # Initialize the stack with an empty list


    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# implementing a stack with a mean method

class StackMin:
    def __init__(self):
        self.super = Stack()
        self.mintracker = Stack()

    def push(self, item):

        # if self.super.size() == 1:
        #     self.mintracker.push(self.super.peek())
        if item <= self.min():
            self.mintracker.push(item)
        self.super.push(item)
    
    def pop(self):
        item = self.super.pop()
        if item == self.min():
            self.mintracker.pop()
        return item

    def min(self):
        if self.mintracker.is_empty():
            return sys.maxsize
        else:
            return self.mintracker.peek()


def nullify_row(mat, row):
    for j in range(len(mat[0])):
        mat[row][j] = 0

def nullify_column(mat, col):
    for i in range(len(mat)):
        mat[i][col] = 0

def nullify_matrix(mat):

    # count rows and columns that have zeros
    row = [0]*(len(mat))
    column = [0]*(len(mat[0]))

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                row[i] = True
                column[j] = True


    # Nullify rows

    for i in range(len(row)):
        if row[i]:
            nullify_row(mat, i)

    # Nullify columns
    for j in range(len(column)):
        if column[j]:
            nullify_column(mat, j)

    return mat

mat = [
    [1, 4, 9, 10],
    [2, 6, 0, 11],
    [10, 14, 2, 9],
    [0, 1, 4, 5]
]

import pprint

element = nullify_matrix(mat)

pp = pprint.PrettyPrinter(compact=True)

pp.pprint(element)