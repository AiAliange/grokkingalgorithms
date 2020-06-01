# -*- coding: utf-8 -*-
def quicksort(arr):
    if len(arr)<=1:
        return arr
    lt,gt = bindiv(arr[1:len(arr)], arr[0])
    return quicksort(lt) + [arr[0]] + quicksort(gt)
    
        
def bindiv(arr,m):
    lt, gt = [],[]
    for i in range(len(arr)):
        if arr[i] > m:
            gt.append(arr[i])
        else:
            lt.append(arr[i])   
    return lt,gt

def main():
    arr = [3,2,5,1,4,7,9,6]
    lt,gt = bindiv(arr[1:len(arr)],arr[0])
    print(lt)
    print(gt)
    print(quicksort(arr))
    
if __name__ == "__main__":
    main()

