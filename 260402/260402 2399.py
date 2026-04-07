import sys

n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
arr.sort()
ans=0
for i, x in enumerate(arr):
    ans += x*(2*i-n+1)
print(ans*2)
