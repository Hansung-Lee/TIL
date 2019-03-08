T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_value = 0
    if N > M:
        for n in range(N-M+1):
            temp = 0
            for m in range(M):
                temp += A[m+n]*B[m]
            if max_value < temp:
                max_value = temp
    else:
        for m in range(M-N+1):
            temp = 0
            for n in range(N):
                temp += A[n]*B[m+n]
            if max_value < temp:
                max_value = temp
                
    print("#{} {}".format(t+1, max_value))