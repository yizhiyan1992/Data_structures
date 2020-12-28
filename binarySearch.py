import bisect
def binarySearch(array,left,right,target):
    """
    :param left: the index of left boundary
    :param right: the index of right boundary
    :param target: value need to be searched
    :return: the index of the value need to be inserted
    """

    if left>right : return left
    middle=left+(right-left)//2
    if array[middle]==target:
        while middle>0 and array[middle-1]==array[middle]:
            middle-=1
        return middle
    elif array[middle]>target:
        return binarySearch(array,left,middle-1,target)
    else:
        return binarySearch(array,middle+1,right,target)

def main():
    arr=[5,7,9,11,13]
    test=[9]
    for i in test:
        idx=binarySearch(arr,0,len(arr)-1,i)
        print(bisect.bisect_left(arr,i))
        print(bisect.bisect_right(arr,i))
        print(idx)
    bisect.insort_left(arr,9)


if __name__=="__main__":
    main()

