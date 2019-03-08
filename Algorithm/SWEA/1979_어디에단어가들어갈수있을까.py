T = int(input())

for t in range(T):
    N, K = map(int, input().split())

    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))

    result = 0
    
    # 가로 탐색
    for i in range(N):
        cnt = 0
        li_cnt = []
        for j in range(N):
            if li[i][j]:
                cnt += 1
            else:
                li_cnt.append(cnt)
                cnt = 0
        li_cnt.append(cnt)
        for c in li_cnt:
            if c == K:
                result += 1

    # 세로 탐색
    for j in range(N):
        cnt = 0
        li_cnt = []
        for i in range(N):
            if li[i][j]:
                cnt += 1
            else:
                li_cnt.append(cnt)
                cnt = 0
        li_cnt.append(cnt)
        for c in li_cnt:
            if c == K:
                result += 1

    print("#{} {}".format(t + 1, result))