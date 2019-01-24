T = int(input())
for t in range(T):
    N = int(input())

    li_panel = [[0]*10 for x in range(10)]

    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                li_panel[i][j] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            if li_panel[i][j]==3:
                cnt+=1
    print(f"#{t+1} {cnt}")