# Recursion -> Divide and Conquer -> Binary Search
def binary_search(arr, start, end, key):
    while start <= end:
        mid = start + int((end-start)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1
arr = [4, 6, 9, 13, 14, 18, 21, 24, 38]
x = 38
binary_search_result = binary_search(arr, 0, len(arr)-1, x)
print(binary_search_result)

# Recursion -> Divide and Conquer -> Merge Sort
def sort_1(arr):
    if len(arr) == 1:
        return arr
    mid = int(len(arr)/2)
    half_1 = arr[:mid]
    half_2 = arr[mid:]
    return sort_2(sort_1(half_1), sort_1(half_2))

def sort_2(half_1, half_2):
    merged_list = []
    i = j = 0
    while i < len(half_1) and j < len(half_2):
        if half_1[i] < half_2[j]:
            merged_list.append(half_1[i])
            i += 1
        else:
            merged_list.append(half_2[j])
            j += 1
    while i < len(half_1):
        merged_list.append(half_1[i])
        i += 1
    while j < len(half_2):
        merged_list.append(half_2[j])
        j += 1
    return merged_list
arr = [3, 4, 2, 23, 43, -2, 3, 1]
merge_sort_result = sort_1(arr)
print(merge_sort_result)

# Dynamic Programming
def dynamic_fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if lookup[i] is not None:
        return lookup[i]
    lookup[i] = dynamic_fibonacci(i-1) + dynamic_fibonacci(i-2)
    return lookup[i]
n = 8
lookup = [None]*(n+1)
for i in range(n):
    dynamic_fibonacci_result = dynamic_fibonacci(i)
    print(dynamic_fibonacci_result)




