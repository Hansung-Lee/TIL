N = int(input())

for n in range(N):
    print(' ' * (N-n-1) + '*' * (n+1))

for n in range(N-2, -1, -1):
    print(' ' * (N-n-1) + '*' * (n+1))