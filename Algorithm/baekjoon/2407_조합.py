n, m = map(int, input().split())

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

answer = int(factorial(n)//(factorial(m)*factorial(n-m)))

print(answer)