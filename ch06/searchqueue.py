# -*- coding: utf-8 -*-
from collections import deque

def search(graph):
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        p= search_queue.popleft()
        if person_is_seller(p):
            print(p + " is a mango seller")
            return True
        else:
            search_queue += graph[p]
    return False
    
def person_is_seller(name):
    return name[-1] == 'm'

def main():
    # 定义一颗树
    g = {}
    g["you"] = ["alice","bob","claire"]
    g["bob"] = ["anuj","peggy"]
    g["alice"] = ["peggy"]
    g["claire"] = ["thom","jonny"]
    g["anuj"] = []
    g["peggy"] = []
    g["thom"] =[]
    g["jonny"] = []
    search(g)
    
if __name__ == "__main__":
    main()
    