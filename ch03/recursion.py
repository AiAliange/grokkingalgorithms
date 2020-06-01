# -*- coding: utf-8 -*-
import os

def displayFloder(dirname,level):
    printname(dirname,level)
        
    files = os.listdir(dirname)
    for f in files:
        fp = dirname+"/"+f
        if os.path.isdir(fp):
            displayFloder(fp,level+1)
        else:
            print(printline(level+1)+f)
            
        
def printname(dirname,level):
    if os.path.isdir(dirname):
        print(printline(level)+"+"+os.path.basename(dirname))
    else:
        print(printline(level)+os.path.basename(dirname))

def printline(n):
    line = ""
    for i in range(n):
        line += "|   "
    return line

def main():
    displayFloder("D:/Prj/py3/grokkingalgorithms",0)
    # print(printline(5))
    
    
if __name__ == '__main__':
    main()