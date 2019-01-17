from fractions import gcd
a,b = map(int, input().split())
print('1' * int(gcd(a,b)))