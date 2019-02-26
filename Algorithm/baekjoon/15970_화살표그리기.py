N = int(input())
li_N = []
for n in range(N):
    li_N.append(list(map(int, input().split())))

li_N.sort()
result = 0

for i in range(len(li_N)):
    min_distance = 999999
    for j in range(i+1, len(li_N)):
        if li_N[i][1] == li_N[j][1]:
            min_distance = li_N[j][0] - li_N[i][0]
            break
    for j in range(i-1, -1, -1):
        if li_N[i][1] == li_N[j][1] and min_distance > li_N[i][0] - li_N[j][0]:
            min_distance = li_N[i][0] - li_N[j][0]
            break

    result += min_distance

print(result)