#use python3
import sys
import threading
import numpy as np

def depth_cal(a):
    #use the recursion to find the max depth O(n)
    if len(a)==1:
        return 1
    else:
        d=[]
        for i in range(1,len(a)):
            d.append(depth_cal(a[i]))
        return 1+max(d)

def tree_depth(data):
    m=len(data)
    nodes=[[i] for i in range(m)]
    for i in range(len(nodes)):
        parent_index=data[i]
        if parent_index==-1:
            root=i
        else:
            #this step is important, because everytime, you append a pointer to the father nodes, which means
            #when the childnode at that list updates, the father, father-father ... nodes will automatically update as well
            nodes[parent_index].append(nodes[i])
    #the list can represent a tree, where the first element is the key, and the following elements are the child nodes
    Tree=nodes[root]
    d=depth_cal(Tree)
    return d

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(tree_depth(parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()