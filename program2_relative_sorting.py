"""
Experiment 7: Hashing and Strings
Program 2: Relative Sorting
Aim: Sort the first array according to the order of the second array.
"""

def relative_sort(a, b):
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    result = []
    for x in b:
        while counts.get(x, 0) > 0:
            result.append(x)
            counts[x] -= 1
    remaining = []
    for x, count in counts.items():
        remaining.extend([x] * count)
    for i in range(1, len(remaining)):
        key = remaining[i]
        j = i - 1
        while j >= 0 and remaining[j] > key:
            remaining[j + 1] = remaining[j]
            j -= 1
        remaining[j + 1] = key
    return result + remaining

print(relative_sort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8], [2, 1, 8, 3]))
