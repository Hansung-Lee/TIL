N = int(input())
cnt=N

for i in range(N):
    for z in range(i):
        print(" ", end='')
    for j in range(cnt):
        print("*", end='')
    cnt-=1
    print('')

