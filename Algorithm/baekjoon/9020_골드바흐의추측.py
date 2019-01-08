T = int(input())

for t in range(T):
    n = int(input())

    cnt = 0
    result = 0
    li = []
    li2 = ["-100000 100000"]

    for num in range(1,n):
        if(num==1):
            pass
        elif(num==2 or num==3 or num==5 or num==7):
            li.append(num)
        elif(num%2==0):
            pass
        else:
            for i in range(3,int(num**0.5)+1,2):
                if(num%i==0):
                    cnt=0
                    break
                cnt+=1
        if(cnt>0):
            li.append(num)
            cnt=0

    breaker = False

    for x in li:
        for y in li:
            if x+y == n:
                if y==li2[-1].split()[0]:
                    breaker = True
                li2.append(f'{x} {y}')
                break
            
        if breaker:
            break

    mindiff = 1000000
    result_idx = 0
    for idx, item in enumerate(li2):
        diff = abs(int(item.split()[0])-int(item.split()[1]))
        if (diff<mindiff):
            mindiff = diff
            result_idx = idx
    
    print(li2[result_idx])