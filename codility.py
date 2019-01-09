
# just exples

def prefix_sums(A):
    n = len(A)
    P = [0]*(n)
    for k in range(n):
        P[k] = P[k-1] + A[k]
    return P

def suffix_sums(A):
    n = len(A)
    P = [0]*(n)
    sum_elements =  sum(A)
    for k in range(n):
        P[k] = sum_elements - sum(A[:k])
    return P

# 1 Binary gap with 100% score

def solution(N):
    """ Return the maximal binary gap"""
    
    # turning N into its binary represenation
    # binary = format(N, 'b')

    # Error case
    if not isinstance(N,int):
        return -1 # Error
   
    max_gap = 0
    current_gap = 0
 
    # Skip the tailing zero(s)
    while N > 0 and N%2 == 0:
        N //= 2
 
    while N > 0:
        remainder = N%2
        if remainder == 0:
            # Inside a gap
            current_gap += 1
        else:
            # Gap ends
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0
        N //= 2
 
    return max_gap


# binary gap 80 %

def max_gab_counter(n):
    binrep = format(n, 'b')
    founded_one = False
    gab_counter = 0
    max_gab = 0
    for i in range (len(binrep)):
        if binrep[i] == '1' and not founded_one:
            founded_one = True
        if binrep[i] == '0' and founded_one:
            gab_counter += 1
        if binrep[i] == '1' and gab_counter:
            max_gab = max(max_gab, gab_counter)
            gab_counter = 0
            founded_one = False
    return max_gab


# 1. Binary Gap

def solution(N):
    """ Return the maximal binary gap"""
    
    # turning N into its binary represenation
    binary = format(N, 'b')
    
    # binary gaps storage list
    result = []
    
    # Creating a temporary list to hold different binary gap
    temp = []
    
    # Toggler that help identify if a gap is being writing or not 
    # and initialize it to False
    opened = False
    
    # Checking for errors
    if type(N) is not int:
        raise TypeError('Argument should be an interger')
    
    # Special cases
    if '0' not in binary:
        return 0
    else:
        for char in binary:
            # check for opening 1
            if char == '1' and not opened:
                opened = True
                continue
            elif char == '1':
                result.append(temp)
                temp = []
            else:
                temp.append(char)
        return result



# 2 cyclic rotation

# 100 % scores

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    
    K = K % len(A)
    return A[-K:] + A[:-K]




def solution(A, K):
    """return a list wich elements are rotated k times"""
    
    # Error cases
    if type(A) is not list or type(K) is not int or K < 0:
        return -1 # errors
    
    if K > len(A):
        return -1
    
    #Edge cases
    if not any(A):
        return A
    
    if len(A) == 1:
        return A

    if K == 0:
        return A

    if K == len(A):
        return A

    if len(A) == 0:
        return A
    #general case
    result = A[:] # copy A
    
    for i in range(len(A)):
        result[i] = A[i-K]
        
    return result


# 3  odd occurences in array

# test scores 100%

def solution(A):
    
    if len(A) == 0:
        return A
        
    A.sort()
    i = 0
    while i < len(A) - 1:
        if A[i] != A[i+1]:
            return A[i]
        i +=2
    return A[len(A)-1]


# another 100 % test score
def solution(A):

    # Error cases
    if not any(isinstance(y, int) for y in A):
        return -1 # all elements in A should be integers
    
    result = 0
    for number in A:
        result ^= number

    return result

# 4 minimum jumps

import math
def solution(X, Y, D):
    """return min jumps count"""
    # Handling assumption
    if type(X) is not int or type(Y) is not int or type(D) is not int:
        return -1 # Errors
    if Y < X :
        return -1 # Errors
    if X == Y:
        return 0
    
    # Determine  jump count value
    min_jump = (Y - X) / D
    
    # return the minimu jump count
    return math.ceil(min_jum)

# 5 Perm missing element

def solution(A):
    """return the missing element in an array"""
    
    # error cases
    if type(A) is not list:
        return -1 # Errors
    # check if all element in A are integers
    if not all(isinstance(x, int) for x in A):
        return -1 # Errors
    
    result = [element for element in range(1, len(A)+1)]
    
    for e in result:
        if e not in A:
            return e
    return False


print(solution([2, 3, 1, 5]))


# 5 perm missing element

from collections import Counter
def solution(A):
    # write your code in Python 3.6
    
    n = len(A) + 1
    
    c = Counter(A)
    
    for ind in range(n):
        el = ind + 1
        
        if el not in c:
            return el
    return 0

# 5 most perfomant version 90% score

def solution(A):
    """return the missing element in an array"""
    
    # error cases
    if len(A) == 0 :
        return 0 

    if len(A) == 1:
        return 1
    
    
    # length of the complete list
    n = len(A) + 1
    
    # determining the lenth of all element together
    sum_result = (n * ( 1 + n)) // 2

    sum_A = sum(A)

    result = sum_result - sum_A

    return result


# 5 perm missing element 100 %

def solution(A):
    # write your code in Python 3.6
    
    N = len(A) + 1
    
    counters = [0] * N
    
    for element in A:
        counters[element - 1] = 1
    
    for index in range(len(counters)):
        if counters[index] == 0:
            return index + 1

# 6 tape equilibrium

def solution(A):
    """return minimum tape differnce"""
    
    # errors
    
    # special cases
    if len(A) == 0 or len(A) == 1:
        return 0 
    
    if len(A) == 2:
        return abs(A[0] - A[1])
    
    # spliter
    p = len(A) - 1
    
    #first element of the list
    head = A[0]


    tail = sum(A[1:])

    min_dif = abs(head - tail)
 
    for index in range(1, p):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
 
    return min_dif


# 7 perm checks

# 100 %
def solution(A):
    counter = [0]*len(A)
    limit = len(A)
    for element in A:
        if not 1 <= element <= limit:
            return 0
        else:
            if counter[element-1] != 0:
                return 0
            else:
                counter[element-1] = 1

    return 1

# 7 second solution with 100 % which is more logical 
def solution(A):
    # write your code in Python 3.6
    counter = [0] * (len(A) + 1)
    for element in A:
        if not 1 <= element <= len(A):
            return 0
        else:
            if counter[element] != 0:
                return 0
            else:
                counter[element] = 1
    return 1


# 8 frog rive one

def solution(X, A):
    covered_time = [-1]*(X+1)  # Record the time, each position is covered
    uncovered = X          # Record the number of uncovered position

    for index in A:
        if covered_time[index] != -1:
            # This position is already covered
            continue
        else:
            # This position is to be covered
            covered_time[index] = index 
            uncovered -= 1
            if uncovered == 0:
                # All positions are covered
                return A.index(index)

    # Finally, some positions are not covered
    return -1

# 8 frog river one another 100% 

def solution(X, A):
    counters = [0] * X

    covered = 0

    for element in A:

        if element > X:
            continue

        if counters[element - 1]:
            continue

        else:
            counters[element - 1] = element
            covered += 1
            if covered == X:
                return A.index(element)
    return -1

# 9 missing integers 

# 100 %

def solution(A):
    # first sort the array to get the numbers in sequence
    A = sorted(A)
    
    # the minimum positive integer that may not be found will be 1
    min_not_found = 1
 
    # loop through the array
    for element in A:
 
        # if the current element is the min_not_found number, move to next number
        if element == min_not_found:
            min_not_found += 1
 
    return min_not_found

# another solution to problem 9, with time complexity = N

def solution(A):
    ''' Solve it with Pigeonhole principle.
        There are N integers in the input. So for the
        first N+1 positive integers, at least one of
        them must be missing.
    '''
    # We only care about the first N+1 positive integers.
    # occurrence[i] is for the integer i+1.
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item-1] = True
    # Find out the missing minimal positive integer.
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1
    return -1
# 10 max counter 66 %

def solution(N, A):
    result = [0]*N
    for command in A:
        if 1 <= command <= N:
            result[command-1] += 1
        else:
            max_counter= max(result)
            result = [max_counter]*N
 
    return result

# 100 % max counter solution

def solution(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
 
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
 
    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
 
    return result


# 11 passing cars 100 %

def solution(A):
#initialize pairs to zero
    pairs = 0
    #count the numbers of zero discovered while traversing 'A'
    #for each successive '1' in the list, number of pairs will
    #be incremented by the number of zeros discovered before that '1'
    east = 0
    #traverse through the list 'A'
    for i in range(0, len(A)):
        if A[i] == 0:
            #counting the number of zeros discovered
            east += 1
        elif A[i] == 1:
            #if '1' is discovered, then number of pairs is incremented
            #by the number of '0's discovered before that '1'
            pairs += east
            #if pairs is greater than 1 billion, return -1
            if pairs > 1000000000:
                return -1
    #return number of pairs
    return pairs

 # second solution passing cars with 100%

 def solution(A):
    west = 0    # The number of west-driving cars so far
    passing = 0 # The number of passing
 
    for index in range(len(A)-1,-1,-1):
        # Travel the list from the end to the beginning
        if A[index] == 0:    # A east-driving car
            passing += west
            if passing > 1000000000:
                return -1
        else:                # A west-driving car
            west += 1
 
    return passing

# a non optimal solution for passing cars

def solution(A):
    li = []
    for q in range(len(A)):
        for p in range(q):
            tup = (A[q], A[p])
            if tup == (1, 0):
                li.append((A[q], A[p]))
    
    if len(li) > 1000000000:
        return -1 
    return len(li)

# 12 div counter 100 %
def div_counter(A, B, K):
    if A%K == 0:
        # (B-(A-A%K))//K + 1 = (B-A)//K + 1
        return (B-A)//K + 1
    else:
        return (B-(A-A%K))//K

# another solution 100 %

def solution(A, B, K):
    count = 0
    counter = A
    while counter <= B:
        if counter % K == 0:
            count = abs(((B-counter)//K)+1)
            break
        elif counter//K == 0:
            counter = K
        else:
            counter = counter + (counter % K)
    return count


# 13 Genomic range query my solution 62 %

def solution(S, P, Q):
    # write your code in Python 3.6
    result = []
    dict = {'A':1, 'C':2, 'G':3, 'T':4}
    m = len(P)
    min_factor = float('inf')
    for k in range(m):
        string = S[P[k]:Q[k] + 1]
        for i in string:
            min_factor = min(min_factor, dict[i])
        result.append(min_factor)
        min_factor = float('inf')
    return result


# 13 simple solution with 100%

def solution(S, P, Q):
    query = []
    for i, j in zip(P, Q):
        sub_S = S[i:j+1]
        if 'A' in sub_S:
            query.append(1)
        elif 'C' in sub_S:
            query.append(2)
        elif 'G' in sub_S:
            query.append(3)
        else:
            query.append(4)
    return query

# 13 second solution with 100%
def prefix_sums(A, mapping):
    n = len(A)
    sums = [[0] * 4 for i in range(n + 1)]
    for k in range(1, n + 1):
        sums[k] = sums[k - 1][:]
        sums[k][mapping[A[k - 1]] - 1] += 1
    return sums

def get_slice_sum(Qi, Pi):
    slice_sum = [0] * len(Qi)
    for i in range(len(Qi)):
        slice_sum[i] = Qi[i] - Pi[i]
    return slice_sum

def solution(S, P, Q):
    mapping = {'A':1, 'C':2, 'G':3, 'T':4}
    sums = prefix_sums(S, mapping)
    result = [0] * len(P)

    for i in range(len(P)):
        slice_sum = get_slice_sum(sums[Q[i] + 1], sums[P[i]])
        if slice_sum[0] != 0:
            result[i] = 1
        elif slice_sum[1] != 0:
            result[i] = 2
        elif slice_sum[2] != 0:
            result[i] = 3
        else:
            result[i] = 4

    return result



# solution 14 minimum average two slices

def solution(A):
    min_avg_value = (A[0] + A[1])/2.0   # The mininal average
    min_avg_pos = 0     # The begin position of the first
                        # slice with mininal average
    for index in range(0, len(A)-2):
        # Try the next 2-element slice
        if (A[index] + A[index+1]) / 2.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1]) / 2.0
            min_avg_pos = index
        # Try the next 3-element slice
        if (A[index] + A[index+1] + A[index+2]) / 3.0 < min_avg_value:
            min_avg_value = (A[index] + A[index+1] + A[index+2]) / 3.0
            min_avg_pos = index
    # Try the last 2-element slice
    if (A[-1]+A[-2])/2.0 < min_avg_value:
        min_avg_value = (A[-1]+A[-2])/2.0
        min_avg_pos = len(A)-2
    return min_avg_pos



# solution 15 on sorting with 100 %

def solution(A):
    if len(A) == 0:
        distinct = 0
    else:
        distinct = 1
        A.sort()
        for index in range(1, len(A)):
            if A[index] != A[index-1]:
                distinct += 1
    return distinct

# solution 15 on distint element 100%

def solution(A):
    # write your code in Python 3.6
    return len(set(A))

# solution 16 max product of three in java, 100%

def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])


# solution 17 max triangle 100%

def solution(A):
    A_len = len(A)
    if A_len < 3:
        # N is an integer within the range [0..1,000,000]
        # if the list is too short, it is impossible to
        # find out a triangular.
        return 0
    A.sort()
    for index in range(0, A_len-2):
        if A[index]+A[index+1] > A[index+2]:
            return 1
        # The list is sorted, so A[index+i] >= A[index+2]
        # where i>2. If A[index]+A[index+1] <= A[index+2],
        # then A[index]+A[index+1] <= A[index+i], where
        # i>=2. So there is no element in A[index+2:] that
        # could be combined with A[index] and A[index+1]
        # to be a triangular.
    # No triangular is found
    return 0


# 17 triangle 100%

def solution(A):
    triangle = 0
    A.sort(reverse=True)
    for j in range(len(A[:-2])):
        if A[j] < A[j+1] + A[j+2]:
            triangle = 1
            break
    return triangle



# stacks

# 19 brackets

def solution(S):
    if len(S) % 2 == 1:   return 0
    matched = {"]":"[", "}":"{", ")": "("}
    to_push = ["[", "{", "("]
    stack = []
    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0


# 20 fish

def solution(A, B):
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream
    downstream_count = 0   # To record the number of elements in downstream
    for index in range(len(A)):
        # Compute for each fish
        if B[index] == 1:
            # This fish is flowing downstream. It would
            # NEVER meet the previous fishs. But possibly
            # it has to fight with the downstream fishs.
            downstream.append(A[index])
            downstream_count += 1
        else:
            # This fish is flowing upstream. It would either
            #    eat ALL the previous downstream-flow fishs,
            #    and stay alive.
            # OR
            #    be eaten by ONE of the previous downstream-
            #    flow fishs, which is bigger, and died.
            while downstream_count != 0:
                # It has to fight with each previous living
                # fish, with nearest first.
                if downstream[-1] < A[index]:
                    # Win and to continue the next fight
                    downstream_count -= 1
                    downstream.pop()
                else:
                    # Lose and die
                    break
            else:
                # This upstream-flow fish eat all the previous
                # downstream-flow fishs. Win and stay alive.
                alive_count += 1
    # Currently, all the downstream-flow fishs in stack
    # downstream will not meet with any fish. They will
    # stay alive.
    alive_count += len(downstream)
    return alive_count

# 21 nesting 100 %

def solution(S):
    parentheses = 0
    for element in S:
        if element == "(":
            parentheses += 1
        else:
            parentheses -= 1
            if parentheses < 0:
                return 0
    if parentheses == 0:
        return 1
    else:
        return 0

# 22 stone wall

def solution(H):
    stack = []
    block_count = 0    # The number of needing blocks
    for height in H:
        while len(stack) != 0 and height < stack[-1]:
            # If the height of current block is less than
            #    the previous ones, the previous ones have
            #    to end before current point. They have no
            #    chance to exist in the remaining part.
            # So the previous blocks are completely finished.
            stack.pop()
            block_count += 1
        if len(stack) == 0 or height > stack[-1]:
            # If the height of current block is greater than
            #    the previous one, a new block is needed for
            #    current position.
            stack.append(height)
        # Else (the height of current block is same as that
        #    of previous one), they should be combined to
        #    one block.
    # Some blocks with different heights are still in the stack.
    block_count += len(stack)
    return block_count


# Leader 

# 23 Dominator

def solution(A):
    # write your code in Python 3.6
    
    half_list = len(A) // 2
    
    dic = {}
    
    for element in A:
        dic[element] = dic.get(element, 0) + 1
        if dic[element] > half_list:
            return A.index(element)
    
    return -1
