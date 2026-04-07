lst=list(map(int,input().split()))
cnt=len(lst)
          
for i in range(cnt-1):
          for j in range(cnt-1):
              if lst[j]>lst[j+1]:
                   lst[j], lst[j+1]=lst[j+1],lst[j]
res=lst[0]*lst[-2]
print(res)
