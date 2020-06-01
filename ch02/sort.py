# -*- coding: utf-8 -*-

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        index = findSmallest(arr)
        newArr.append(arr[index])
        arr.pop(index)
    return newArr

arr = [1,3,8,5,2,4,6]
print(selectionSort(arr))