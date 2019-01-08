N = int(input())

li_num = map(int,input().split())

result = 0
cnt = 0

for num in li_num:
    if(num==1):
        pass
    elif(num==2):
        result+=1
    else:
        for i in range(2,num):
            if(num%i==0):
                cnt=0
                break
            cnt+=1
    if(cnt>0):
        result+=1
        cnt=0
print(result)