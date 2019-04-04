T = int(input())

for t in range(T):
    N = int(input())
    li = [[5]*(N+2)]
    for n in range(N):
        temp = list(map(int, input().split()))
        temp.insert(0, 5)
        temp.append(5)
        li.append(temp)
    li.append([5]*(N+2))

    max_value = 0
    direction = 0  # 0:동, 1:서, 2:남, 3:북

    holes = [[] for _ in range(11)]
    blacks = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            if li[i][j] in [6, 7, 8, 9, 10]:
                holes[li[i][j]].append([i, j])
            elif li[i][j] == -1:
                blacks.append([i, j])

    for i in range(1, N+1):
        for j in range(1, N+1):
            if li[i][j] == 0:
                for q in range(4):
                    direction = q
                    temp = 0
                    now = [i, j]
                    start = [i, j]
                    while True:
                        if direction == 0:
                            now[1] += 1
                        elif direction == 1:
                            now[1] -= 1
                        elif direction == 2:
                            now[0] += 1
                        elif direction == 3:
                            now[0] -= 1
                        
                        if li[now[0]][now[1]] == 1:
                            temp += 1
                            if direction == 0:
                                direction = 1
                            elif direction == 1:
                                direction = 3
                            elif direction == 2:
                                direction = 0
                            elif direction == 3:
                                direction = 2
                        elif li[now[0]][now[1]] == 2:
                            temp += 1
                            if direction == 0:
                                direction = 1
                            elif direction == 1:
                                direction = 2
                            elif direction == 2:
                                direction = 3
                            elif direction == 3:
                                direction = 0
                        elif li[now[0]][now[1]] == 3:
                            temp += 1
                            if direction == 0:
                                direction = 2
                            elif direction == 1:
                                direction = 0
                            elif direction == 2:
                                direction = 3
                            elif direction == 3:
                                direction = 1
                        elif li[now[0]][now[1]] == 4:
                            temp += 1
                            if direction == 0:
                                direction = 3
                            elif direction == 1:
                                direction = 0
                            elif direction == 2:
                                direction = 1
                            elif direction == 3:
                                direction = 2
                        elif li[now[0]][now[1]] == 5:
                            temp += 1
                            if direction == 0:
                                direction = 1
                            elif direction == 1:
                                direction = 0
                            elif direction == 2:
                                direction = 3
                            elif direction == 3:
                                direction = 2
                        elif li[now[0]][now[1]] in [6, 7, 8, 9, 10]:
                            for h in holes[li[now[0]][now[1]]]:
                                if now != h:
                                    now = h[:]
                                    break
                        elif li[now[0]][now[1]] == -1 or now == start:
                            break

                    if max_value < temp:
                        max_value = temp

    print("#{} {}".format(t+1, max_value))