# -*- coding: utf-8 -*-
def binarysearch(arr, l, h, v):
    m = (l+h)//2
    if arr[m] == v:
        return m
    elif arr[m] > v:
        return binarysearch(arr,l,m,v)
    else:
        return binarysearch(arr,m,h,v)
    
def main():
    arr = [1,2,3,4,5,6,7,8]
    print(binarysearch(arr,0,len(arr),8))

if __name__ == "__main__":
    main()
