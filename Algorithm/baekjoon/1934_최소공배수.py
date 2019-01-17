# 최대 공약수 유클리드 호제법
def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

# 최소 공배수
def lcm(a, b):
    return a*b//gcd(a,b)


T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    print(lcm(a,b))