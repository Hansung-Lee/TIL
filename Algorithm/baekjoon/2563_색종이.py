li = [[0]*101 for _ in range(101)]

N = int(input())

for n in range(N):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            li[i][j] = 1

print(sum([sum(x) for x in li]))