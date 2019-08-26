#use python3
import queue

def processing(size,ope):
    m=len(ope)
    Q=queue.Queue(size)
    result=[]
    end_time=[]
    for i in range(m):
        # dequeue: eliminate all elements already processed
        if Q.empty() == False:
            while end_time != [] and ope[i][0] >= end_time[0]:
                del end_time[0]
                Q.get()
        #enqueue
        if Q.full():
            result.append(-1)
        else:
            # enqueue conflict, if there are multiple commands at the same time, the time to enqueue should be delayed
            if i>0 and ope[i][0]==ope[i-1][0]:
                ope[i][0]=ope[i][0]+ope[i-1][1]
            # judge the time to process, the time to enqueue is not the time to processing
            if end_time!=[] and end_time[-1]>ope[i][0]:
                ope[i][0]=end_time[-1]
            end_time.append(ope[i][0]+ope[i][1])
            result.append(ope[i][0])
            Q.put(ope[i])

    return result
if __name__=='__main__':
    size,command=list(map(int,input().split()))
    ope=[]
    for i in range(command):
        ope.append(list(map(int,input().split())))
    result=processing(size,ope)
    for i in range(len(result)):
        print(result[i],end='\n')