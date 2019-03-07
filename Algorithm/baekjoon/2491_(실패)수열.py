def check_asc(li):
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            return False
    return True

def func(n):
    for i in range(N-n+1):
        if check_asc(li[i:i+n]) or check_asc(li[i:i+n][::-1]):
            return n
    if n > 1:
        return func(n-1)
    
N = int(input())
li = list(map(int, input().split()))

print(func(N))