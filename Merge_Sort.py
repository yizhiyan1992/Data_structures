# sort the array and combine them
def merge(array1,array2):
        merge_array=[]
        while array1!=[] and array2!=[]:
                if array1[0]<array2[0]:
                        k=array1.pop(0)
                        merge_array.append(k)
                else:
                        k=array2.pop(0)
                        merge_array.append(k)
        if array1!=[]:
                merge_array=merge_array+array1
        if array2!=[]:
                merge_array=merge_array+array2
        return merge_array

#use the recurrence to partition the array (binary partition)
def array_divide(array,left,right):
        if left>=right:
                return
        middle=left+(right-left)//2
        array_divide(array,left,middle)
        array_divide(array,middle+1,right)
        left_array=array[left:middle+1]
        right_array=array[middle+1:right+1]
        array[left:right+1]=merge(left_array,right_array)
        return

def merge_sort(array,left,right):
        array_divide(array,left,right)
        return array

if __name__=="__main__":
        n=int(input())
        array=list(map(int,input().split()))
        left=0;right=n-1
        print(merge_sort(array,left,right))
