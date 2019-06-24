

# id 1

def find_sum(n):
    """find multiple of 5 and 3 
    below 1000"""
    sum = 0
    for e in range (n):
        if e % 5 == 0 or e % 3 == 0:
            sum += e
    return sum

# id 2, sum of fibonacci numbers
def fib(n):
    """ fib of n n is an integer """
    if n <= 2:
        return 1 
    return fib(n-1) + fib(n-2)

def memo_fib(n, memo={0:0, 1:1}):
    """Another version of determining fib numbers
using memoisaion"""
    if n not in memo:
        memo[n] = memo_fib(n-1, memo) + memo_fib(n-2, memo)
    return memo[n]

print(memo_fib(10))

def iter_fib(n):
    """Return fib sequence in a more efficient way"""
    fibs = [1, 2]
    for i in range(3,n):
        res = fibs[-1] + fibs[-2]
        fibs.append(res)
    return fibs


def fib_sequence(n):
    """Find Fibonacci sequence for large integers in python
    using for or while loops
    Because recursive depth is less than 1000"""
    result = []
    e = 1
    i = 1
    j = 1
    while e <= n:
        result.append(i)
        i, j = j, i+j
        e += 1
    return result

def fibonacci(n):
    """return fibonacci value of a given number"""
    seq = fib_sequence(n)
    number = seq[-1]
    return number


def sum_fib(n):
    """ fib values do not exceed n 
    and find sum of even-valued terms"""
    total = 0
    for e in fib_sequence(100):    
        if  e % 2 == 0 and e < n:
            print (e)
            total += e
    return total

print (sum_fib(4000000))
print fibonacci(10)
print fib(10)



# id 3

import math

# By the fundamental theorem of arithmetic, every integer n > 1 has a unique factorization as a product of prime numbers.
# In other words, the theorem says that n = p_0 * p_1 * ... * p_{m-1}, where each p_i > 1 is prime but not necessarily unique.
# Now if we take the number n and repeatedly divide out its smallest factor (which must also be prime), then the last
# factor that we divide out must be the largest prime factor of n. For reference, 600851475143 = 71 * 839 * 1471 * 6857.

# The prime factors of 13195 are 5, 7, 13 and 29.

def prime_factors(n):
    result = []
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            result.append(p)
            n //= p
        else:
            result.append(n)
            return result


def largest_prime_factor(n):
	# n = 600851475143
	while True:
		p = smallest_prime_factor(n)
		if p < n:
			n //= p
		else:
			return str(n)


# Returns the smallest factor of n, which is in the range [2, n]. The result is always prime.

def smallest_prime_factor(n):
    assert n >= 2
    s = int(round(math.sqrt(n)))
    for e in range(2, s + 1):
        if n % e == 0:
            return e
    return n   # n itself 

print (largest_prime_factor(600851475143))
    



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

    
#  id 4
def largest_palindrome(n):
    '''return the largest palindrome product of the
    product of 2 n-digits numbers'''
    max_num = int('9'*n)
    min_num = int('9'*(n-1))

    i = max_num
    j = min_num

    re = []

    for i in range(max_num, min_num, -1):
        for j in range(max_num, min_num, -1):
            result = i*j
            temp = str(result)
            if is_palindrome(temp):
                re.append(int(temp))
    print (re)
    return max(re)

def is_palindrome(st):
    ''' Take a string a return wether is it a
    palindrome or not'''
    li = []
    for i in st:
        li.append(i)

    li.reverse()
    s1 = ''.join(li)
    if st == s1:
        return True
    return False


print (largest_palindrome(3))

def greatest_palindrome():
	ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
    
	return str(ans)

