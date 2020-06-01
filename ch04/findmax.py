# -*- coding: utf-8 -*-
def findmax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        m = arr[0]
        arr1 = arr[1:len(arr)]
        t = findmax(arr1)
        if m > t:
            return m
        else:
            return t

def main():
    arr = [2,6,3,9,4,1]
    print(findmax(arr))
    
if __name__ == "__main__":
    main()