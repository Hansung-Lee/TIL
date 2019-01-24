N = int(input())

dp = [999999]*(N+1)
dp[0] = 0
dp[1] = 1

for i in range(2,len(dp)):
    for j in range(int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-(j**2)]+1)

print(dp[N])