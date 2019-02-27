T = int(input())

for t in range(T):
    N = int(input())
    li_C = []
    li_G = []
    for n in range(N):
        msg = input().split()
        li_C.append(int(msg[0]))
        li_G.append(float(msg[1]))
    
    result = 0.0

    for i in range(N):
        result += li_G[i]*li_C[i]

    print(f"{sum(li_C)} {round(result/sum(li_C), 1)}")