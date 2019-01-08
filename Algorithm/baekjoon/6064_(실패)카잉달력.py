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

# 메모리 초과
#################################################
# 시간 초과

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
    
    gap = M-N
    limit = int(lcm(M,N)/M)

    li_kaing=[]

    a=x

    for i in range(limit):
        li_kaing.append(f'{x}:{a}')
        for r in range(abs(gap)):
            if(gap > 0):
                a+=1
            elif(gap < 0):
                a-=1
            if (a==N+1):
                a=1
            elif(a==0):
                a=N
    
    if(f'{x}:{y}' in li_kaing):
        print((li_kaing.index(f'{x}:{y}')*M)+x)
    else:
        print('-1')