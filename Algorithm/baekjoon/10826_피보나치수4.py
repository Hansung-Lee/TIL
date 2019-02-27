N = int(input())

if N == 0:
    print(0)
else:
    dp = [-1] * (N+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(0, N+1):
        if i >= 2:
            dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])