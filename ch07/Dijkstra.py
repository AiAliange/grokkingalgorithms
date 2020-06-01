# -*- coding: utf-8 -*-
class node:
    def __init__(self, name, parent, val):
        self.name = name
        self.parent = parent
        self.val = val

def nodes(graph, start):
    ns = {}
    for k in graph.keys():
        if k != start:
            ns[k] = node(k, "", float("inf"))
    for k in graph[start].keys():
        ns[k].parent = start
        ns[k].val = graph[start][k]
    for k in ns.keys():
        costs.append(ns[k])

def minnode(costs):
    c = None
    mv = float('inf')
    for n in costs:
        if  n.name in processed:
            continue
        if n.val < mv:
            c = n
            mv = n.val
    return c



graph = {}
costs = []
wait_process = []
processed = []
def searchminnode():
    m = minnode(costs)
    if m == None:
        return
    if m.name in processed:
        return
    processed.append(m.name)
    for zi in graph[m.name].keys():
        for n in costs:
            if zi == n.name:
                v = m.val + graph[m.name][zi]
                if v < n.val:
                    n.val = v
                    n.parent = m.name
    searchminnode()     
    return

def graph1():
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["end"]=1
    graph["b"] = {}
    graph["b"]["a"]=3
    graph["b"]["end"]=5
    graph["end"] = {}

def graph2():
    graph["start"] = {}
    graph["start"]["A"] = 5
    graph["start"]["B"] = 2
    graph["A"] = {}
    graph["A"]["C"] = 4
    graph["A"]["D"] = 2
    graph["B"] = {}
    graph["B"]["A"] = 8
    graph["B"]["D"] = 7
    graph["C"] = {}
    graph["C"]["D"] = 6
    graph["C"]["end"] = 3
    graph["D"] = {}
    graph["D"]["end"] = 1
    graph["end"] = {}

def printcosts():
    for c in costs:
        print(c.parent, c.name, c.val)

def main():
    graph2()
    print(graph)
    nodes(graph, "start")
    for k in graph.keys():
        if k != "start":
            wait_process.append(k)
    print(wait_process)
    searchminnode()
    printcosts()
    return
    
if __name__ == "__main__":
    main()