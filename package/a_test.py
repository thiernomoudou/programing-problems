def merge_count(unsorted, max_score):
    counter = [0] * (max_score + 1)
    for item in unsorted:
        counter[item] += 1

    indices = []
    
    before_count = 0
    for element in counter:
        indices.append(before_count)
        before_count += element

    sorted = [None] * (len(unsorted))

    for element in unsorted:
        sorted[indices[element]] = element
        indices[element] += 1
    
    sorted.reverse()
    return sorted