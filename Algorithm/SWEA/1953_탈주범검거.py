def bfs(dx, dy):
    global visited

    for q in range(len(dx)):
        new_x = x + dx[q]
        new_y = y + dy[q]
        tf = False

        if 0 <= new_x < N and 0 <= new_y < M:
            if dx[q] == 0 and dy[q] == -1:
                if li[new_x][new_y] in [1,3,4,5]:
                    tf = True
            elif dx[q] == 0 and dy[q] == 1:
                if li[new_x][new_y] in [1,3,6,7]:
                    tf = True
            elif dx[q] == -1 and dy[q] == 0:
                if li[new_x][new_y] in [1,2,5,6]:
                    tf = True
            elif dx[q] == 1 and dy[q] == 0:
                if li[new_x][new_y] in [1,2,4,7]:
                    tf = True
            
        if tf and not visited[new_x][new_y]:
            queue.append((new_x, new_y, d+1))
            visited[new_x][new_y] = True
            

T = int(input())

for t in range(T):
    N, M, R, C, L = map(int, input().split())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))
    
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not li[i][j]:
                visited[i][j] = True

    queue = [(R, C, 1)]
    visited[R][C] = True
    cnt = 0

    while queue:
        x, y, d = queue.pop(0)
        cnt += 1

        if d != L:
            if li[x][y] == 1:
                dx = [0, 0, -1, 1]
                dy = [-1, 1, 0, 0]
                bfs(dx, dy)
            elif li[x][y] == 2:
                dx = [-1, 1]
                dy = [0, 0]
                bfs(dx, dy)
            elif li[x][y] == 3:
                dx = [0, 0]
                dy = [-1, 1]
                bfs(dx, dy)
            elif li[x][y] == 4:
                dx = [0, -1]
                dy = [1, 0]
                bfs(dx, dy)
            elif li[x][y] == 5:
                dx = [0, 1]
                dy = [1, 0]
                bfs(dx, dy)
            elif li[x][y] == 6:
                dx = [0, 1]
                dy = [-1, 0]
                bfs(dx, dy)
            elif li[x][y] == 7:
                dx = [0, -1]
                dy = [-1, 0]
                bfs(dx, dy)

    print("#{} {}".format(t+1, cnt))