M = int(input())
N = int(input())
li = [[0],[0]]
li[0].extend(list(map(int, input().split())))
li[1].extend(list(map(int, input().split())))
li[0].append(0)
li[1].append(0)

dp = [0] * (N+2)
dp_member = [[]] * (N+2)

for i in range(1,N+2):
    min_value = 99999999
    min_member = []
    distance = 0
    for j in range(i, 0, -1):
        distance += li[0][j]
        if distance > M:
            break
        else:
            temp = dp[j-1]+li[1][i]
            temp_member = dp_member[j-1][:]
            temp_member.append(i)
            if min_value > temp:
                min_value = temp
                min_member = temp_member[:]
    dp[i] = min_value
    dp_member[i] = min_member[:]

if dp[N+1]:
    print(dp[N+1])
    print(len(dp_member[N+1][:-1]))
    print(' '.join(map(str, dp_member[N+1][:-1])))
else:
    print(dp[N+1])
    print(len(dp_member[N+1][:-1]))