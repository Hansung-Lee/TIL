def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    answer = int(factorial(M)//(factorial(N)*factorial(M-N)))
    print(answer)