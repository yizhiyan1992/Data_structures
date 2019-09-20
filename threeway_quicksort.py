#use python3
import numpy as np

def threeway_quicksort(array,left,right):
        if left>=right:
                return
        rand=np.random.randint(left,right+1)
        array[rand],array[right]=array[right],array[rand]
        pivot=array[right]
        b1=left;b2=right-1
        i=left
        while i<=b2:
                if array[i]<pivot:
                        array[i],array[b1]=array[b1],array[i]
                        b1+=1
                        i+=1
                elif array[i]==pivot:
                        i+=1
                elif array[i]>pivot:
                        array[i],array[b2]=array[b2],array[i]
                        b2-=1
        array[b2+1],array[right]=array[right],array[b2+1]
        threeway_quicksort(array,left,b1-1)
        threeway_quicksort(array,b2+1,right)

if __name__=="__main__":
        array=list(map(int,input().split()))
        left=0;right=len(array)-1
        threeway_quicksort(array,left,right)
        print(array)




