n=int(input())
people=set()
for _ in range(n):
    name, status=input().split()
    
    if status=='enter':
        people.add(name)
    else:
        people.remove(name)
        
print(*sorted(people, reverse=True), sep='\n')
