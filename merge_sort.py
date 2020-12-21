
def merge(left,right):
    if not left or not right: return left+right
    p1=p2=0
    res=[]
    while p1<len(left) and p2<len(right):
        if left[p1]<right[p2]:
            res.append(left[p1])
            p1+=1
        else:
            res.append(right[p2])
            p2+=1
    if p1<len(left):
        res+=left[p1:]
    if p2<len(right):
        res+=right[p2:]

    return res

def merge_sort(array,left,right):
    if left==right:
        return [array[left]]
    middle=left+(right-left)//2
    left=merge_sort(array,left,middle)
    right=merge_sort(array,middle+1,right)
    #print(left,right)
    return merge(left,right)

arr=[7,1,3]
arr=merge_sort(arr,0,len(arr)-1)
print(arr)