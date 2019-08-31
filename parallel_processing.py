#use python3
import heapq
def thread(i):
    #end time/ id/ start time
    return [0,i,0]

def processing(threads,command):
    heapq.heapify(threads)
    record=[]
    for i in range(len(command)):
        u=heapq.heappop(threads)
        u[2]=u[0]
        u[0]=u[0]+command[i]
        record.append([u[1],u[2]])
        heapq.heappush(threads,u)
    return record
if __name__=='__main__':
    m,n=list(map(int,input().split()))
    threads=[]
    for i in range(m):
        threads.append(thread(i))
    command=list(map(int,input().split()))
    record=processing(threads,command)
    for i in record:
        print(i[0],i[1],end='\n')