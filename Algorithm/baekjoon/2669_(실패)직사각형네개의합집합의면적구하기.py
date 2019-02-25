square = list(map(int, input().split()))
square.extend(list(map(int, input().split())))
square.extend(list(map(int, input().split())))
square.extend(list(map(int, input().split())))

N = max(square)+1

li = [[0]*N for x in range(N)]

for n in range(0, len(square), 4):
    x = (square[n], square[n+1])
    y = (square[n+2], square[n+3])

    for i in range(x[0],y[0]):
        for j in range(x[1],y[1]):
            li[i][j] += 1

result = 0

for i in range(len(li)):
    for j in range(len(li[0])):
        if li[i][j] > 0:
            result +=1

print(result)