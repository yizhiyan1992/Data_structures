#use python3
import queue

def stack(command,key):
    m=len(command)
    S=queue.LifoQueue()
    max_value=[]
    result=[]
    for i in range(m):
        if command[i]=='push':
            u=key.pop(0)
            S.put(u)
            if max_value==[]:
                max_value.append(u)
            # consider the case that there might be same max values stacking in it, so it should be <= instead of <
            elif max_value[-1]<=u:
                max_value.append(u)
        if command[i]=='pop':
            u=S.get()
            if max_value[-1]==u:
                del max_value[-1]
        if command[i]=='max':
            result.append(max_value[-1])
    return result
if __name__=="__main__":
    m=int(input())
    command=[]
    key=[]
    for i in range(m):
        data=input().split()
        command.append(data[0])
        if data[0]=='push':
            key.append(int(data[1]))
    result=stack(command,key)
    for i in range(len(result)):
        print(result[i],end='\n')