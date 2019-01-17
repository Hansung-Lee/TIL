T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li_N = list(map(int, input().split()))

    max_value = 0
    min_value = 10001*M
    
    for i in range(N-M+1):
        value = 0
        for j in range(M):
            value += li_N[i+j]
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    print (f"#{t+1} {max_value-min_value}")