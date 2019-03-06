N = int(input())
li = [[0] * 101 for _ in range(101)]

for n in range(N):
    a, b, c, d = map(int, input().split())

    for i in range(a,a+c):
        for j in range(b,b+d):
            li[i][j] += (10**n)

area_N = [0] * N

for i in range(101):
    for j in range(101):
        for q in range(N):
            if 10**q<= li[i][j] < 10**(q+1):
                area_N[q] += 1
                break

for n in area_N:
    print(n)