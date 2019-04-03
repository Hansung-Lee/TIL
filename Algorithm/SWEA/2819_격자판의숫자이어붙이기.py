T = int(input())

for t in range(T):
    li = []
    for _ in range(4):
        li.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    result = []

    for i in range(4):
        for j in range(4):
            stack = [(i, j, 0)]
            temp = [''] * 7

            while stack:
                x, y, d = stack.pop()
                temp[d] = str(li[x][y])
                if d == 6:
                    result.append(''.join(temp))
                else:
                    for q in range(4):
                        new_x = x + dx[q]
                        new_y = y + dy[q]

                        if 0 <= new_x < 4 and 0 <= new_y < 4:
                            stack.append((new_x, new_y, d+1))
    result = list(set(result))

    print("#{} {}".format(t+1, len(result)))