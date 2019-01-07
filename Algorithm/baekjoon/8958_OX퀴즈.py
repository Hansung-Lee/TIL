N = int(input())

li=[]

for i in range(N):
    li.append(input())

score = 1
sum = 0

for j in li:
    score = 1
    sum = 0
    for ox in j:
        if(ox=='O'):
            sum+= score
            score+=1
        elif(ox=='X'):
            score=1
    print(sum)