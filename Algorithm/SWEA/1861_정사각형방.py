T = int(input())

for t in range(T):
    N = int(input())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))
    
    max_depth = 0
    result = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            queue = [(i, j, 1)]

            while queue:
                x, y, d = queue.pop(0)

                if max_depth < d:
                    max_depth = d
                    result = li[i][j]
                elif max_depth == d and result > li[i][j]:
                    result = li[i][j]

                for q in range(4):
                    new_x = x + dx[q]
                    new_y = y + dy[q]

                    if 0 <= new_x < N and 0 <= new_y < N:
                        if li[x][y]+1 == li[new_x][new_y]:
                            queue.append((new_x, new_y, d+1))
                            break

    print("#{} {} {}".format(t+1, result, max_depth))