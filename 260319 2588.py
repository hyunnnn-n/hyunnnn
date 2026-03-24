a=int(input())
b=str(input())
c=[]
for i in range(len(b)):
    c.append(a*int(b[len(b)-i-1]))
d=0
e=0
for j in c:
    print(j)
    d+=j*(10**e)
    e+=1
print(d)
