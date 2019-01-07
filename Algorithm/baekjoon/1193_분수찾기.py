N = int(input())

direction = False  # True => right, False => left

X = 1
Y = 1

limit = 0
cnt = 0

for i in range(N-1):
    if(direction):
        if (cnt==limit):
            cnt = 0
            limit+=1
            X+=1
            direction = False
        else:
            X+=1
            Y-=1
            cnt+=1
    else:
        if(cnt==limit):
            cnt = 0
            limit+=1
            Y+=1
            direction = True
        else:
            X-=1
            Y+=1
            cnt+=1
        


print(f"{X}/{Y}")