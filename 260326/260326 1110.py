n=int(input())
s=n
count=0

while 1:
    a=s//10
    b=s%10
    s=(a+b)%10+b*10
    count+=1
    if s == n:
        break
print(count)
