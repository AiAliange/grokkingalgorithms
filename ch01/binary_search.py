# -*- coding: utf-8 -*-
def binary_search(llist, item):
    low =0
    high = len(llist) - 1
    
    while low <= high:
        mid = int((low + high)/2)
        guess = llist[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid+1;
    return None

my_list = [1,2,3,4,5,6,7]
result = binary_search(my_list, 6)
print(result)
print(pow(2,7))