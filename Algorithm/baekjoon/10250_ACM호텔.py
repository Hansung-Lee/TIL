T = int(input())

for t in range(T):
    H, W, N = map(int, input().split())

    for i in range(N):
        X=1+N//H
        Y=N%H
        if(Y==0):
            Y=H
            X-=1

    if(X<10):
        print(f"{Y}0{X}")
    else:
        print(f"{Y}{X}")