T = int(input())

for t in range(T):
    N = int(input())
    farm = []

    for n in range(N):
        msg = input()
        farm.append([int(x) for x in msg])

    for i in range(N//2):
        for j in range((N//2) - i -1, -1, -1):
            farm[i][j] = 0
        for j in range((N//2) + i + 1, N):
            farm[i][j] = 0

    for i in range(N-1, N//2, -1):
        for j in range((N//2) - (N-1 - i) -1, -1, -1):
            farm[i][j] = 0
        for j in range((N//2) + (N-1 - i) +1, N):
            farm[i][j] = 0

    print("#{} {}".format(t+1, sum([sum(x) for x in farm])))