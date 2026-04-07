n=int(input())
for i in range(n):
    s=input()
    stack=[]
    res='NO'
    for j in s:
        if j=='(':
            stack.append(j)
        elif j==')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(j)
    if len(stack)==0:
        res='YES'
    print(res)
