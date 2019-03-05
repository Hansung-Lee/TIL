def hap(stand, idx):
    global sum_

    x = dices[idx]
    y = []
    for p in set_:
        if x.index(stand) in p:
            for q in range(len(x)):
                if q in p:
                    pass
                else:
                    y.append(x[q])
    sum_ += max(y)


N = int(input())
dices = []
set_ = [[1, 3], [2, 4], [0, 5]]

for n in range(N):
    dices.append(list(map(int, input().split())))

max_value = 0
sum_ = 0

for i in range(6):
    stand = dices[0][i]
    sum_ = 0
    hap(stand, 0)

    for j in range(1, N):
        hap(stand, j)
        for p in set_:
            if dices[j].index(stand) in p:
                stand = dices[j][p[p.index(dices[j].index(stand)) - 1]]
                break

    if max_value < sum_:
        max_value = sum_

print(max_value)