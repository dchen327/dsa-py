'''
Python implementation of quicksort

Quicksort is a fast sorting algorithm that takes a divide-and-conquer approach to sorting lists.
'''


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # pick pivot as middle element
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # recursively sort the parts
    return quicksort(left) + mid + quicksort(right)