import numpy as np
def quick_sort(array,left,right):
    if left>=right: return
    rd=np.random.randint(left,right+1)
    array[left],array[rd]=array[rd],array[left]
    pivot=array[left]
    l=left
    r=right
    while l<r:
        #start from right side (p.s. we must start from the right side, it not, then the pivot element could swap with the element that is larget than it.
        while array[r]>=pivot and l<r:
            r-=1
        while array[l]<=pivot and l<r:
            l+=1
        #swap
        array[l],array[r]=array[r],array[l]
    #swap the pivot with the right pointer
    array[left],array[r]=array[r],array[left]
    quick_sort(array,left,r-1)
    quick_sort(array,r+1,right)
    return


def main():
    array = [1, 6, 6, 0, 10, 10, 2, 3, 4, 4, 4, 7, 5, 1, 4, 2, 3]
    quick_sort(array, 0, len(array) - 1)
    print(array)


if __name__=="__main__":
    main()
