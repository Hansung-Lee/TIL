def check_garo(blueprint):
    s = blueprint[0]
    garo = []
    sero = []
    for q in range(len(blueprint)):
        if blueprint[q][0] == s[0]:
            garo.append(blueprint[q])
        elif blueprint[q][0] == s[0]+1 or blueprint[q][0] == s[0]-1:
            sero.append(blueprint[q])
    if len(garo) == 1 and len(sero) == 4:
        for q in range(len(blueprint)):
            if blueprint[q][0] == s[0]-2 or blueprint[q][0] == s[0]+2:
                garo.append(blueprint[q])
    if len(garo) == 4 and len(sero) == 2:
        garo.sort()
        if s in garo:
            print(garo[garo.index(s)-2][2])
        else:
            print(sero[garo.index(s)-1][2])
        return True
    else:
        if len(sero) == 4 and len(garo) == 2:
            sero.sort()
            if s in sero:
                print(sero[sero.index(s) - 2][2])
            else:
                print(garo[garo.index(s) - 1][2])
            return True
        else:
            return False

def check_sero(blueprint):
    s = blueprint[0]
    garo = []
    sero = []
    for q in range(len(blueprint)):
        if blueprint[q][1] == s[1]:
            sero.append(blueprint[q])
        elif blueprint[q][1] == s[1]+1 or blueprint[q][1] == s[1]-1:
            garo.append(blueprint[q])
    if len(sero) == 1 and len(garo) == 4:
        for q in range(len(blueprint)):
            if blueprint[q][1] == s[1]-2 or blueprint[q][1] == s[1]+2:
                sero.append(blueprint[q])
    if len(sero) == 4 and len(garo) == 2:
        sero.sort()
        if s in sero:
            print(sero[sero.index(s)-2][2])
        else:
            print(garo[garo.index(s)-1][2])
        return True
    else:
        if len(garo) == 4 and len(sero) == 2:
            garo.sort()
            if s in garo:
                print(garo[garo.index(s) - 2][2])
            else:
                print(sero[sero.index(s) - 1][2])
            return True
        else:
            return False

li = []

for i in range(6):
    li.append(list(map(int, input().split())))

start = (0, 0, 1)

for i in range(6):
    for j in range(6):
        if li[i][j] == 1:
            start = (i, j, 1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        if li[i][j] == 0:
            visited[i][j] = True

stack = [start]
visited[start[0]][start[1]] = True
result = []
result.append(start)

while stack:
    x, y, data = stack.pop()
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]

        if 0 <= a < 6 and 0 <= b < 6:
            if not visited[a][b]:
                stack.append((a, b, li[a][b]))
                visited[a][b] = True
                result.append((a, b, li[a][b]))

if len(result) == 6:
    if check_garo(result) or check_sero(result):
        pass
    else:
        print(0)
else:
    print(0)