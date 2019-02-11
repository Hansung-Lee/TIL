N = int(input())
li_P = list(map(int, input().split()))

dp = li_P[:]

for i in range(1, N):
    for j in range(i):
        dp[i] = max(dp[i-j-1]+li_P[j], dp[i])

print(dp[N-1])