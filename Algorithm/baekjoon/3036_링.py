def gcd(a, b):
    mod = a%b
    while mod > 0:
        a = b
        b = mod
        mod = a%b
    return b

N = int(input())
li_N = list(map(int, input().split()))

for i in range(1,N):
    i_gcd = gcd(li_N[0],li_N[i])
    print(f"{li_N[0]//i_gcd}/{li_N[i]//i_gcd}")