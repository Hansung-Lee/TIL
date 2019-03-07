N, M = map(int, input().split())
maze = [[0]*(M+1)]

for n in range(N):
    temp_li = [0]
    temp_li.extend(list(map(int,list(input()))))
    maze.append(temp_li)

visited = [[False] * (M+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(M+1):
        if not maze[i][j]:
            visited[i][j] = True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = [(1, 1, 1)]
visited[1][1] = True

result = ''

while queue:
    point = queue.pop(0)
    result = point

    if point[0] == N and point[1] == M:
        break

    for i in range(4):
        x = point[0] + dx[i]
        y = point[1] + dy[i]

        if 0 < x <= N and 0 < y <= M:
            if not visited[x][y]:
                queue.append((x, y, point[2]+1))
                visited[x][y] = True

print(result[2])