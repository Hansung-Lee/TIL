T = int(input())

for t in range(T):
    n = int(input())
    li = []
    for i in range(2):
        li.append(list(map(int, input().split())))
    
    dp = [[0]*n, [0]*n]

    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0]

    dp[0][1] = li[1][0] + li[0][1]
    dp[1][1] = li[0][0] + li[1][1]
    

    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1]+li[0][i], dp[1][i-2]+li[0][i])
        dp[1][i] = max(dp[0][i-1]+li[1][i], dp[0][i-2]+li[1][i])
    
    print(max(dp[0][n-1], dp[1][n-1]))