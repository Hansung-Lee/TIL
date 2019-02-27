def turn_mat(li):
    result = [[0] * N for x in range(N)]
    a = b = 0

    for j in range(N):
        for i in range(N-1, -1, -1):
            result[a][b] = li[i][j]
            b = (b+1) % N
        a = (a+1) % N

    return result

T = int(input())

for t in range(T):
    N = int(input())
    li_N = []
    for n in range(N):
        li_N.append(list(map(int, input().split())))
    
    result = [""] * N

    for q in range(3):
        li_N = turn_mat(li_N)
        for x in range(N):
            for y in range(N):
                result[x] += str(li_N[x][y])
            result[x] += " "

    print(f"#{t+1}")
    for x in range(N):
        print(result[x])