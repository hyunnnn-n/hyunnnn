N=int(input())
book=[]
for _ in range(N):
    s=input()
    flag=False
    for b in book:
        if b[0]==s:
            flag=True
            b[1]+=1
            break
    if not flag:
        book.append([s,1])
        
book.sort(key=lambda x: [-x[1],x[0]])

print(book[0][0])
