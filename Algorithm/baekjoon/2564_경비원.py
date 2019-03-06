G, S = map(int, input().split())
store_N = int(input())
li = []
set_ = [[1,2], [3,4]]

for n in range(store_N):
    li.append(list(map(int, input().split())))

a, b = map(int, input().split())
DG = (a, b)

result = 0

for i in li:
    if i[0] == DG[0]:
        result += abs(DG[1]-i[1])
    elif [i[0], DG[0]] in set_ or [DG[0], i[0]] in set_:
        if DG[0] == 1 or DG[0] == 2:
            result += min(DG[1]+i[1]+S, (G-DG[1])+(G-i[1])+S)
        elif DG[0] == 3 or DG[0] == 4:
            result += min(DG[1]+i[1]+G, (S-DG[1])+(S-i[1])+G)
    else:
        if DG[0] == 1 and i[0] == 3:
            result += (i[1]+DG[1])
        elif DG[0] == 1 and i[0] == 4:
            result += (i[1]+(G-DG[1]))
        elif DG[0] == 2 and i[0] == 3:
            result += ((S-i[1])+DG[1])
        elif DG[0] == 2 and i[0] == 4:
            result += ((S-i[1])+(G-DG[1]))
        elif DG[0] == 3 and i[0] == 1:
            result += (i[1]+DG[1])
        elif DG[0] == 3 and i[0] == 2:
            result += (i[1]+(S-DG[1]))
        elif DG[0] == 4 and i[0] == 1:
            result += (DG[1]+(G-i[1]))
        elif DG[0] == 4 and i[0] == 2:
            result += ((G-i[1])+(S-DG[1]))

print(result)