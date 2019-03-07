T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))

    max_value = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for m1 in range(M):
                for m2 in range(M):
                    temp += li[i+m1][j+m2]
            if max_value < temp:
                max_value = temp

    print("#{} {}".format(t+1,max_value))