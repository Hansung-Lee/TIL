import sys

T = int(sys.stdin.readline())

# 최대 공약수
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


for j in range(T):
    M, N, x, y = map(int,sys.stdin.readline().split())
    li_kaing=[]
    a=b=1
    for i in range(lcm(M,N)):
        if(a<=M and b<=N):
            li_kaing.append(f'{a}:{b}')
            a+=1
            b+=1
        elif(a>M):
            a=1
            li_kaing.append(f'{a}:{b}')
            a+=1
            b+=1
        elif(b>N):
            b=1
            li_kaing.append(f'{a}:{b}')
            a+=1
            b+=1
    try:
        print(li_kaing.index(f'{x}:{y}')+1)
    except:
        print('-1')