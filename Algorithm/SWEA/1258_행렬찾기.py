T = int(input())

for t in range(T):
    N = int(input())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))

    visited = [[False] * N for x in range(N)]

    for i in range(N):
        for j in range(N):
            if li[i][j] == 0:
                visited[i][j] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    result = []

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                queue = [(i, j)]
                temp_li = [(i, j)]
                visited[i][j] = True

                while queue:
                    a, b = queue.pop(0)
                    for q in range(4):
                        x = a + dx[q]
                        y = b + dy[q]
                        if x >= 0 and y >= 0 and x < N and y < N:
                            if not visited[x][y]:
                                queue.append((x, y))
                                temp_li.append((x, y))
                                visited[x][y] = True
                temp_li.sort()
                result.append([temp_li[-1][0] - temp_li[0][0] + 1, temp_li[-1][1] - temp_li[0][1] + 1])

    answer = f"{len(result)} "

    for j in range(len(result)-1):
        for i in range(len(result)-1):
            if result[i][0]*result[i][1] > result[i+1][0]*result[i+1][1]:
                result[i], result[i+1] = result[i+1], result[i]
            elif result[i][0]*result[i][1] == result[i+1][0]*result[i+1][1]:
                if result[i][0] > result[i+1][0]:
                    result[i], result[i+1] = result[i+1], result[i]


    for r in result:
        answer += f"{r[0]} {r[1]} "

    print(f"#{t+1} {answer}")