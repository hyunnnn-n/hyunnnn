T=int(input())

for i in range(T):
    quiz=str(input())
    answer=0
    t=1
    
    for j in range(len(quiz)):
        if quiz[j]=='O':
            answer += t
            t+=1
        else:
            t=1
    print(answer)
