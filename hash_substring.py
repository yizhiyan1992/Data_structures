#use python3
def Poly_Hash(word,x,p):
        length=len(word)
        hash_number=0
        for i in range(length):
                hash_number=hash_number*x+ord(word[length-i-1])
                hash_number=hash_number%p
        return hash_number

def naive_search(a,b):
        return a==b

def RabinKarp(word,string):
        x=1;p=1000000019;
        criteria=Poly_Hash(word,x,p)
        result=[]
        L_word=len(word);L_string=len(string)
        H=[None for _ in range(L_string-L_word+1)]
        H[-1]=Poly_Hash(string[L_string-L_word:],x,p)
        y=x**L_word
        if H[-1]==criteria and word==string[L_string-L_word:]:
                result.append(L_string-L_word)
        for i in range(len(H)-1):
                H[len(H)-1-i-1]=H[len(H)-1-i]*x-ord(string[len(H)-1-i-1+L_word])*y+ord(string[len(H)-1-i-1])
                H[len(H)-1-i-1]=H[len(H)-1-i-1]%p
                if H[len(H)-1-i-1]!=criteria:
                        continue
                if word==string[len(H)-1-i-1:len(H)-1-i-1+L_word]:
                        result.append(len(H)-1-i-1)
        return result

if __name__=="__main__":
        word=input()
        string=input()
        result=RabinKarp(word,string)
        result.reverse()
        for i in result:
                print(i,end=' ')
