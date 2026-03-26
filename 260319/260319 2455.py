sum=0
pe=[]
maxi=0
li=[]
for i in range(4):
    a,b=map(int,input().split())
    sum=sum-a+b
    pe.append(sum)
    
print(max(pe))
