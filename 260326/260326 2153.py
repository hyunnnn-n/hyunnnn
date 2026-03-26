from math import sqrt
word=input()

num=0
for i in word:
    temp=ord(i)
    if 97<= temp <= 122:
        num += (temp - 96)
    elif 65 <= temp <= 90:
        num += (temp-38)

for i in range(2, int(sqrt(num))+1):
    if num%1==0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")
