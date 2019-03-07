def dfs():
    global tf
    visitied = [[False] * 6 for _ in range(12)]
    tf = False

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(12):
        for j in range(6):
            if li[i][j] == ".":
                visitied[i][j] = True

    for i in range(12):
        for j in range(6):
            result = []
            if not visitied[i][j]:
                stack = [(i, j, li[i][j])]
                visitied[i][j] = True

                while stack:
                    point = stack.pop()
                    result.append([point[0], point[1]])

                    for q in range(4):
                        x = point[0] + dx[q]
                        y = point[1] + dy[q]

                        if 0 <= x < 12 and 0 <= y < 6:
                            if not visitied[x][y] and li[x][y] == point[2]:
                                stack.append((x, y, li[x][y]))
                                visitied[x][y] = True

            if len(result) >= 4:
                for q in result:
                    li[q[0]][q[1]] = "."
                tf = True


li = []
tf = True

for _ in range(12):
    li.append(list(input()))

result = 0

while tf:
    dfs()
    for i in range(12):
        for j in range(6):
            if li[i][j] == '.':
                for q in range(i, 0, -1):
                    li[q][j], li[q-1][j] = li[q-1][j], li[q][j]
    if tf:
        result += 1

print(result)