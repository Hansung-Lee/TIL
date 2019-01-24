T = int(input())
A = [i for i in range(1,13)]

for t in range(T):
    N, K = map(int, input().split())
    cnt = 0

    temp_li = []

    for i in range(1<<12):
        result = 0
        temp_li.clear()
        for j in range(12):
            if i & (1<<j):
                temp_li.append(j+1)
                result += j+1
        if len(temp_li) == N and result == K:
            cnt+=1

    print(f"#{t+1} {cnt}")