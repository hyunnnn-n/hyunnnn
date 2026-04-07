import sys
input=sys.stdin.readline

maxNum=-1
location=0

for order in range(1,10):
    n=int(input())
    if n>maxNum:
        maxNum=n
        location=order
        
print(maxNum)
print(location)
