n = 1
while(n!=0):
    n = int(input())

    cnt = 0
    result = 0

    for num in range(n+1,(2*n)+1):
        if(num==1):
            pass
        elif(num==2 or num==3 or num==5 or num==7):
            result+=1
        elif(num%2==0):
            pass
        else:
            for i in range(3,int(num**0.5)+1,2):
                if(num%i==0):
                    cnt=0
                    break
                cnt+=1
        if(cnt>0):
            result+=1
            cnt=0

    if(n!=0):
        print(result)