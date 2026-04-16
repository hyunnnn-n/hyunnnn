is_self=[1]*20000

def d(num):
    num_str=str(num)
    num_len=len(num_str)
    sum=0
    
    for i in range(num_len):
        sum+=int(num_str[i])
        
    is_self[sum+num]=0
    
for i in range(10000):
    d(i+1)
 
for i in range(10000):
    if is_self[i+1]==1:
        print(i+1)
