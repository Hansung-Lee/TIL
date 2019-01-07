N = int(input())

li = []

sum = 1

if(N==1):
    print(1)

else:
    for i in range(30):
        sum+=i*6
        li.append(sum)

    for k in li:
        if(N<=k):
            print(li.index(k)+1)
            break
    print(li)