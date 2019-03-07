for t in range(10):
    T = int(input())
    li = []

    for _ in range(100):
        li.append(list(map(int, input().split())))

    min_cnt = [99999, -1]

    for j in range(100):
        cnt = 999999
        if li[0][j] == 1:
            cnt = 1
            n = [0, j]
            visited = [[False] * 100 for _ in range(100)]

            for i in range(99):
                n = [n[0]+1, n[1]]
                cnt += 1
                visited[n[0]][n[1]] = True

                while True:
                    if n[1] > 0 and li[n[0]][n[1]-1] == 1 and not visited[n[0]][n[1]-1]:
                        n[1] -= 1
                        cnt += 1
                        visited[n[0]][n[1]] = True
                    elif n[1] < 99 and li[n[0]][n[1]+1] == 1 and not visited[n[0]][n[1]+1]:
                        n[1] += 1
                        cnt += 1
                        visited[n[0]][n[1]] = True
                    else:
                        break
        if min_cnt[0] >= cnt:
            min_cnt[0] = cnt
            min_cnt[1] = j

    print("#{} {}".format(T, min_cnt[1]))