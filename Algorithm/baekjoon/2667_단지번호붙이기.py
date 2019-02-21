N = int(input())
li_N = []

for n in range(N):
    msg = input()
    li_N.append([int(x) for x in msg])

visited = [[False] * N for x in range(N)]

for i in range(N):
    for j in range(N):
        if li_N[i][j] == 0:
            visited[i][j] = True

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

stack = []
li_result = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            stack.append((i, j))
            result = 0
            while stack:
                x, y = stack.pop()
                for a in range(4):
                    x1 = x + dx[a]
                    y1 = y + dy[a]
                    if x1 >=0 and y1>=0 and x1<N and y1<N:
                        if visited[x1][y1] == False:
                            visited[x1][y1] = True
                            result +=1
                            stack.append((x1, y1))
            if result == 0:
                li_result.append(1)
            else:
                li_result.append(result)

li_result.sort()
print(len(li_result))
for result in li_result:
    print(result)