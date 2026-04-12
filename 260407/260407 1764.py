import sys
n,m=map(int,input().split())

people=set()

for _ in range(n):
    person=sys.stdin.readline().rstrip()
    people.add(person)
    
result=[]

for _ in range(m):
    person=sys.stdin.readline().rstrip()
    if person in people:
        result.append(person)
        
result.sort()

print(len(result))
print(*result, sep='\n')
