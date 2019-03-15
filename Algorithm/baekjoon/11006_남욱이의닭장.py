T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    U = 2*M-N
    print(U,M-U)