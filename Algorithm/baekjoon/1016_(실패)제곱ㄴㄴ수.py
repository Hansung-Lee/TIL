min_, max_ = map(int,input().split())

li = []
result = 0

for num in range(2,int(max_**0.5)+1):
    tf = True
    if(num==2):
        li.append(num)
    elif(num%2==0):
        continue
    else:
        for i in range(3,int(num**0.5)+1,2):
            if(num%i==0):
                tf = False
                break
        if tf:
            li.append(num)

for i in range(min_,max_+1):
    for su in li:
        if i%(su**2)==0:
            result += 1
            break  
print(max_-min_+1-result)