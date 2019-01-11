N, K = map(int, input().split())

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

if K>N:
    print (0)
elif K<0:
    print (0)
else:
    print (int(factorial(N)/(factorial(K)*factorial(N-K))))