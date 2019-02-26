N, M, H = map(int, input().split())

li_garo = []
li_sero = []

for n in range(N+1):
    li_garo.append(list(map(int, input().split())))

for n in range(N):
    li_sero.append(list(map(int, input().split())))

result = 0

for i in range(N):
    for j in range(M):
        result += min(li_garo[i][j] if li_garo[i][j]>0 else 10000, li_garo[i+1][j] if li_garo[i+1][j]>0 else 10000, li_sero[i][j] if li_sero[i][j]>0 else 10000, li_sero[i][j+1] if li_sero[i][j+1]>0 else 10000)

print(result)