T = int(input())

for t in range(T):
    N = int(input())
    result = []
    for n in range(1, N+1):
        result.append([1]*n)

    if N >= 3:
        for j in range(2, N):
            for i in range(1, j):
                result[j][i] = result[j-1][i]+result[j-1][i-1]

    print("#{}".format(t+1))
    for r in result:
        print(' '.join([str(x) for x in r]))