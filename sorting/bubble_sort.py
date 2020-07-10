'''
Python implementation of bubble sort

From brilliant.org:

Bubble sort is a comparison​-based algorithm that compares each pair of elements in an array and swaps 
them if they are out of order until the entire array is sorted. For each element in the list, the algorithm 
compares every pair of elements.

It's also horribly inefficient, although it is super simple to understand and implement
'''


def bubble_sort(arr):
    swapped = True  # boolean flag to break out of the loop if more sorting is unnecessary
    while swapped:
        swapped = False
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swaps
                    swapped = True
