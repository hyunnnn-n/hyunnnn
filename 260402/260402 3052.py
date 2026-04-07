A=[]
for _ in range(10):
    n=int(input())
    A.append(n%42)
print(len(set(A)))
