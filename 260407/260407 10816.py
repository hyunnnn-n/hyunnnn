import sys

N=int(sys.stdin.readline())
card=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
check=list(map(int, sys.stdin.readline().split()))

count_dict={}

for c in card:
    count_dict[c]=count_dict.get(c,0)+1
    
result=[]
for i in check:
    result.append(str((count_dict.get(i,0))))
    
print(' '.join(result))
