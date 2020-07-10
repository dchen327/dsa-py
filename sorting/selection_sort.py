'''
Python implementation of selection sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
'''


def selection_sort(arr):
    n = len(arr)
    # outer loop controls the base comparisons to find the mininum number to swap out
    for i in range(n):
        minimum = arr[i]
        # only want to work with the numbersafter the base comparison, avoid comparing n with n
        for j in range(1, n - i):
            if arr[i + j] < minimum:
                minimum = arr[i + j]
        min_index = arr[i:].index(minimum) + i
        # swaps mininum values with the base
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



