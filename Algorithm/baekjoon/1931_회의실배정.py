N = int(input())

li = []

for n in range(N):
    a, b = map(int, input().split())
    li.append([b,a])

li.sort()

result = [[-1,-1]]

for i in range(len(li)):
    if result[-1][0] <= li[i][1]:
        result.append(li[i])

print(len(result)-1)
