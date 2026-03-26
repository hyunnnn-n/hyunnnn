time=list(map(int,input().split()))
time1=int(input())
time2=time1%3600
hour=(time1//3600)+time[0]
min=(time2//60)+time[1]
sec=(time2%60)+time[2]
print(((sec//60+min)//60+hour)%24,(sec//60+min)%60,sec%60)
