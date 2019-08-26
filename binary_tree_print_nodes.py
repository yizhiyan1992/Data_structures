#use python3
import queue

class Node:
    def __init__(self,key):
        self.key=key
        self.left_child=None
        self.right_child=None

class tree:
    def __init__(self,node=None):
        tree.root=node

    def add_node(self,item):
        node=Node(item)
        if self.root==None:
            self.root=node
            return
        else:
            Q=queue.Queue()
            Q.put(self.root)
            while not Q.empty():
                u=Q.get()
                if u.left_child==None:
                    u.left_child=node
                    return
                elif u.right_child==None:
                    u.right_child=node
                    return
                else:
                    Q.put(u.left_child)
                    Q.put(u.right_child)

    def in_order_traverse(self,node,in_order):
        #change the sequence of append to realize post_traverse and pre_traverse
        if node==None:
            return
        self.in_order_traverse(node.left_child,in_order)
        in_order.append(node.key)
        self.in_order_traverse(node.right_child,in_order)
        return in_order

    def breadth_search(self,node,breadth):
        Q=queue.Queue()
        Q.put(node)
        while not Q.empty():
            u=Q.get()
            breadth.append(u.key)
            if u.left_child!=None:
                Q.put(u.left_child)
            if u.right_child!=None:
                Q.put(u.right_child)
        return breadth

if __name__=="__main__":
    #input 1 2 3 4 5 6 7 8 for example
    data=list(map(int,input().split()))
    BinaryTree=tree()
    order=[]
    breadth=[]
    for i in range(len(data)):
        BinaryTree.add_node(data[i])
    print(BinaryTree.in_order_traverse(BinaryTree.root,order))
    print(BinaryTree.breadth_search(BinaryTree.root, breadth))

