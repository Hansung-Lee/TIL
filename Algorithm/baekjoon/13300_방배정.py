N, K = map(int, input().split())

li = [[0]*7 for _ in range(2)]

for n in range(N):
    a, b = map(int, input().split())
    li[a][b] += 1

cnt = 0

for i in range(len(li)):
    for j in range(len(li[0])):
        if li[i][j]%K:
            cnt = cnt + (li[i][j]//K) + 1
        else:
            cnt = cnt + (li[i][j]//K)

print(cnt)