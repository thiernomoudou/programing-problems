#

# Merging a list keeping it sorted

import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    print(heap)
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list



print(merge([[13, 5, 2], [1, 18, 4], [9, 6, 90]]))

# climbing staicase

   def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)


def staircase_cahed(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        print(cache)
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    return cache[-1]

print(staircase_cahed(5, {1,3,5}))
