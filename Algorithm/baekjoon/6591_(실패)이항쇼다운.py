def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

while(True):
    n, k = map(int, input().split())
    if (n+k)==0:
        break
    print(factorial(n)//(factorial(k)*(factorial(n-k))))