def count_house(i, j, r):
    result = 0

    for q in range((r//2)+1):
        if q == 0:
            if 0 <= i < N and 0 <= j < N:
                result += li[i][j]
        else:
            if 0 <= i < N and 0 <= j-q < N:
                result += li[i][j-q]

            if 0 <= i < N and 0 <= j+q < N:
                result += li[i][j+q]

    return result


def check(i, j, k):
    result = 0

    for q in range(k):
        result += count_house(i-q, j, k-(q*2))

    for q in range(1, k):
        result += count_house(i+q, j, k-(q*2))

    return result


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))

    result = 0

    for k in range(1, 2*N):
        expenses = k*k + (k-1)*(k-1)

        for i in range(N):
            for j in range(N):
                temp = check(i, j, (k*2)-1)
                revenue = temp*M

                if revenue >= expenses and result < temp:
                    result = temp

    print("#{} {}".format(t+1, result))
