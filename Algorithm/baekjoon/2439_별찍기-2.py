N = int(input())
li = []
cnt=N

for i in range(N):
    for j in range(cnt-1):
        print(" ", end='')
    for z in range(i+1):
        print("*", end='')
    cnt-=1
    print('')

