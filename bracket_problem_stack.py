#use python3
import queue
def bracket(data):
    result='Success'
    m=len(data)
    data_index=[[data[i],i] for i in range(m)]
    Q=queue.LifoQueue()
    for i in range(m):
        if data_index[i][0]=='[' or data_index[i][0]=='{' or data_index[i][0]=='(':
            Q.put(data_index[i])
        elif data_index[i][0]==']':
            if Q.empty()==True:
                result=i+1
                break
            u = Q.get()
            if u[0]!='[':
                result=i+1
                break
        elif data_index[i][0]=='}':
            if Q.empty()==True:
                result=i+1
                break
            u=Q.get()
            if u[0]!='{':
                result=i+1
                break
        elif data_index[i][0]==')':
            if Q.empty()==True:
                result=i+1
                break
            u=Q.get()
            if u[0]!='(':
                result=i+1
                break
    if result=='Success' and Q.empty()==False:
        result=Q.get()[1]+1
    return result

if __name__=='__main__':
    data=input()
    m=len(data)
    data_list=[]
    for i in range(m):
        data_list.append(data[i])
    print(bracket(data_list))
