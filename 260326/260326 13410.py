import sys

N,K=map(int,sys.stdin.readline().split())

def reverse_gugudan(n,k):
    nums=[]
    for i in range(1,k+1):
        nums.append(n*i)
    reverse_nums=[]
    for num in nums:
        str_num=""
        for c in str(num):
            str_num=c+str_num
        reverse_nums.append(int(str_num))
    reverse_nums.sort()
    return reverse_nums

print(reverse_gugudan(N,K)[-1])
