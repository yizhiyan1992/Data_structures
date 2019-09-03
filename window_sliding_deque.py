#use python3
A=[5,6,4,8,10,12,3,5,9]
k=3
def window_sliding(A,k):
    deque=[]
    max_val=[]
    for i in range(k):
        if i==0:
            deque.append(i)
        else:
            deque.append(i)
            while len(deque)>1 and A[deque[-2]]<A[i]:
                del deque[-2]
    max_val.append(A[deque[0]])
    for i in range(k,len(A)):
        while len(deque)>=1 and deque[0]<=i-k:
            del deque[0]
        deque.append(i)
        while len(deque) > 1 and A[deque[-2]] < A[i]:
            del deque[-2]
        max_val.append(A[deque[0]])
    return max_val
if __name__=="__main__":
    width=int(input())
    sequence=list(map(int,input().split()))
    window=int(input())
    result=window_sliding(sequence,window)
    for i in result:
        print(i,end=' ')