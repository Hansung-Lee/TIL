N, K = map(int, input().split())

coins = []

for n in range(N):
    coins.append(int(input()))

coins = coins[::-1]

cnt = 0

for i in range(len(coins)):
    if K >= coins[i]:
        cnt += (K//coins[i])
        K-= (K//coins[i])*coins[i]
    if K == 0:
        break

print(cnt)
