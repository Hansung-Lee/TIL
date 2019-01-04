import sys

N, X = map(int, sys.stdin.readline().split())

Y = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if Y[i] < X:
        print(Y[i], end=" ")