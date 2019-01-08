M, N = map(int, input().split())

cnt = 0

for num in range(M,N+1):
    if(num==1):
        pass
    elif(num==2 or num==3 or num==5 or num==7):
        print(num)
    elif(num%2==0):
        pass
    else:
        for i in range(3,int(num**0.5)+1,2):
            if(num%i==0):
                cnt=0
                break
            cnt+=1
    if(cnt>0):
        print(num)
        cnt=0