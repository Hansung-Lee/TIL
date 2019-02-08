n, m = map(int, input().split(':'))

def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

print(f"{n//gcd(n,m)}:{m//gcd(n,m)}")