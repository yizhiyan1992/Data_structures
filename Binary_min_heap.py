# use python3
def extractmin(point,i):
    k=point[i]
    point[i]=point[0]
    point[0]=k
    point=siftdown(point,0,i)
    return point

def siftdown(point,i,p):
    size=p
    maxindex=i
    l=2*i+1
    # this step is important. consider the case that a node may only have left child but not right child, so the left
    # and right cases should be considered separately.
    if l<=size-1 and point[l]<point[maxindex]:
        maxindex=l
    r=2*i+2
    if r<=size-1 and point[r]<point[maxindex]:
        maxindex=r
    if i!=maxindex:
        k=point[i]
        point[i]=point[maxindex]
        point[maxindex]=k
        siftdown(point,maxindex,p)
    return point
def HeapSort(point):
    size=len(point)
    swap=[]
    for i in range(size):
        point=siftdown(point,size-i-1,size)
    for i in range(size):
        point=extractmin(point,size-i-1)
    return point



if __name__=='__main__':
    #print 5 7 4 1 9 10 for example
    Point=list(map(int,input().split()))
    point=HeapSort(Point)
    print(point)