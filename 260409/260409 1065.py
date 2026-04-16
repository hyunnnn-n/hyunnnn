n=int(input())
lst=[]
cnt=0
for i in range(1,n+1):
  if i<=99:
      cnt+=1
  else:
      lst+=list(str(i))
      a,b,c=lst.pop(0),lst.pop(0),lst.pop(0)
      if int(a)-int(b)==int(b)-int(c):
          cnt+=1

print(cnt)
