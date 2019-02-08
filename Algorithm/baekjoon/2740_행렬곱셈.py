N, M = map(int, input().split())
mat_A = []

for n in range(N):
    mat_A.append(list(map(int, input().split())))

M, K = map(int, input().split())
mat_B = []

for m in range(M):
    mat_B.append(list(map(int, input().split())))

mat_result = [[0]*K for x in range(N)]

for i in range(N):
    for j in range(K):
        temp_value = 0
        for p in range(M):
            temp_value += mat_A[i][p]*mat_B[p][j]
        mat_result[i][j] = temp_value

for n in range(N):
    print(' '.join(list(map(str, mat_result[n]))))