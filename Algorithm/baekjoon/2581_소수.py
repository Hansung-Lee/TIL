M = int(input())
N = int(input())

cnt = 0
li = []

for num in range(M,N+1):
    if(num==1):
        pass
    elif(num==2):
        li.append(num)
    else:
        for i in range(2,num):
            if(num%i==0):
                cnt=0
                break
            cnt+=1
    if(cnt>0):
        li.append(num)
        cnt=0

if(li):
    print(sum(li))
    print(min(li))
else:
    print('-1')