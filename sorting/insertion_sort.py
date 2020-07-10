'''
Python implementation of insertion sort

From brilliant.org:

Insertion sort is a comparison-based algorithm that builds a final sorted array one element at a time. 
It iterates through an input array and removes one element per iteration, finds the place the element 
belongs in the array, and then places it there.
'''


def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        # shift elements greater than curr to the right, so we can insert curr before them
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr  # j + 1 because we decrement j the line above

    return arr