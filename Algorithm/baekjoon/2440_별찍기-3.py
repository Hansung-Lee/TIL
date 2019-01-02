N = int(input())
cnt=N

for i in range(N):
    for j in range(cnt):
        print("*", end='')
    cnt-=1
    print('')

