# -*- coding: utf-8 -*-
def sum(arr,level):
    s = arr[0]
    if len(arr) > 2:
        arr1 = arr[1:len(arr)]
        print(level)
        s +=sum(arr1,len(arr1))
    else:
        s += arr[1]
    print(level)
    return s
    
def main():
    s = [1,2,3,4,5]
    print(sum(s,len(s)))
    
if __name__ == "__main__":
    main()
