try:
    while True:
        N = int(input())

        if N < 2:
            print(1)

        else:
            dp = [-1] * (N+1)
            dp[0] = 0
            dp[1] = 1
            dp[2] = 3

            for i in range(3, N+1):
                dp[i] = dp[i-1] + (dp[i-2]*2)

            print(dp[N])
except:
    pass