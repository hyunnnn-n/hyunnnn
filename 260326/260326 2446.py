import sys
input=sys.stdin.readline
n=int(input())
i=0
for x in range(n*2-1):
    print(' '*i+'*'*(n*2-1-2*i))
    if x < n-1:
        i += 1
    else:
        i -= 1
