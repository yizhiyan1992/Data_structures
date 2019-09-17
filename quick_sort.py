# QuickSort
import numpy as np
def Quick_Sort(array,left,right):
    if left>=right: #warning, do not use left==right, because pivot-1 can be -1 in the recurrence
        return
    # find a random number as the pivot element
    rand=np.random.randint(left,right+1)
    pivot=array[rand]
    T=array[right]
    array[right]=array[rand]
    array[rand]=T
    pivot_index=left
    # linear scan all elements (exclude the last element, i.e pivot element)
    for i in range(right-left):
        if array[left+i]<=pivot:
            T=array[left+i]
            array[left+i]=array[pivot_index]
            array[pivot_index]=T
            pivot_index+=1

    # change the position of pivot element
    T=array[right]
    array[right]=array[pivot_index]
    array[pivot_index]=T
    # use recurrence
    Quick_Sort(array,left,pivot_index-1)
    Quick_Sort(array,pivot_index+1,right)


if __name__=="__main__":
    array=list(map(int,input().split()))
    left = 0;right = len(array) - 1
    Quick_Sort(array,left,right)
    print(array)