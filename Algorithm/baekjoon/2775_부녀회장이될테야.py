T = int(input())

def f(k,n):
    if (n==1):
        return 1
    elif(k==0):
        return n
    else:
        return f(k-1,n) + f(k,n-1)


for t in range(T):
    k = int(input())
    n = int(input())

    print(str(f(k,n)))