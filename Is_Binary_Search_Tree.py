#use python3
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def Inorder_traversal(node,key,traverse,Binary):
    if node[key][1]!=-1:
        if node[node[key][1]][0]==node[key][0]:
            Binary[0]=False
        Inorder_traversal(node,node[key][1],traverse,Binary)
    traverse.append(node[key][0])
    if node[key][2]!=-1:
        Inorder_traversal(node,node[key][2],traverse,Binary)

def main():
    N=int(input())
    #Binary is the criteria to see if the tree violate the rule of Node.left==Node
    #Order is the list to guarantee the In_order traversal is non-decreasing
    node=[];key=0;pre=[];inorder=[];Binary=[True];Order=True
    for i in range(N):
        node.append(list(map(int,input().split())))
    if node!=[]:
        Inorder_traversal(node,key,inorder,Binary)
    for i in range(1,len(inorder)):
        if inorder[i]<inorder[i-1]:
            Order=False
    #print(' '.join(list(map(str,inorder))))
    if Order and Binary[0]:
        print('CORRECT')
    else:
        print('INCORRECT')

threading.Thread(target=main).start()