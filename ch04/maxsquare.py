# -*- coding: utf-8 -*-
def maxsquare(a,b):
    l,w = 0,0
    if a > b:
        l, w = a, b
    else:
        l, w = b, a
    if l == w:
        return w
    else:
        x = l % w
        if x == 0:
            return w
        else:
            return maxsquare(w,x)

def main():
    l, w = 1680, 640
    a = maxsquare(l,w)
    print((l/a)*(w/a))
    
if __name__ == "__main__":
    main()
    
        
