N = int(input())
li = []
result1 = []
result2 = []

for n in range(N):
    li.append(list(map(int, input().split())))

for i in range(len(li)):
    for j in range(len(li[len(li)-1-i])):
        if i == 0:
            result1.append(li[len(li)-1-i][j])
        else:
            result1.append(max(result2[i-1][j], result2[i-1][j+1]) + li[len(li)-1-i][j])
    result2.append(result1[:])
    result1.clear()

print(result2[-1][0])