import numpy as np
"""
implementation of min-heap class
which support three methods:
        1) heapify
        2) push
        3) pop

"""



class min_heap:
    def __init__(self):
        return


    def heapify(self,array):
        new_arr=[]
        for ele in array:
            self.push(new_arr,ele)
        for i in range(len(array)):
            array[i]=new_arr[i]
        return

    def push(self,array,element):
        array.append(element)
        self.sift_up(array)
        return

    def pop(self,array):
        if len(array)==0:
            return array
        size=len(array)
        array[0],array[size-1]=array[size-1],array[0]
        pop_ele=array.pop()
        #sift down
        self.sift_down(array)
        return pop_ele

    def sift_down(self,array):
        father_idx=0

        while True:
            left_idx = father_idx * 2 + 1
            right_idx = father_idx * 2 + 2
            if left_idx>=len(array):
                break
            left_val=float('inf')
            right_val=float('inf')

            if left_idx<len(array):
                left_val=array[left_idx]
            if right_idx<len(array):
                right_val=array[right_idx]
            if array[father_idx]<left_val and array[father_idx]<right_val:
                break
            if left_val<right_val:
                array[father_idx],array[left_idx]=array[left_idx],array[father_idx]
                father_idx=left_idx
            else:
                array[father_idx], array[right_idx] = array[right_idx], array[father_idx]
                father_idx=right_idx
        return

    def sift_up(self,array):
        p=len(array)-1
        while True:
            if p<=0: break
            father=(p-1)//2
            if father>=0 and array[p]<=array[father]:
                array[p],array[father]=array[father],array[p]
                p=father
            else:
                break
        return

def main():
    arr=np.random.randint(0,100,20)
    mh = min_heap()
    mh.heapify(arr)
    print(arr)
    """
    pq=[]
    for i in arr:
        mh.push(pq,i)
    print(pq)
    while pq:
        print(mh.pop(pq))
    """

if __name__=="__main__":
    main()