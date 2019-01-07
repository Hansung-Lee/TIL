T = int(input())

li = []

limit = 1
num = 1
cnt = 1

for q in range(1000):
    if(cnt == limit):
        for i in range(limit):
            li.append(num)
        num+=1
        for i in range(limit):
            li.append(num)
        limit+=1
    else:
        num +=1
        cnt +=1

for t in range(T):
    x, y = map(int, input().split())
    distance = y-x
    print(li[distance-1])