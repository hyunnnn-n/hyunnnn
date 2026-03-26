N,X=map(int,input().split())
A=list(map(int,input().split()))
n=[]
for i in range(N):
    if A[i]<X:
        n.append(A[i])
        
print(" ".join(map(str,n)))
