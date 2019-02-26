li = []
result = []

def search_garo(li):
    global result
    result = []
    max_value = 0
    for i in range(len(li)):
        temp_result = [(0, 0), (0, 0), (0, 0)]
        for j in range(len(li)):
            if li[i][j] == 1:
                temp_result[0] = (i, j)
                break
        for j in range(len(li) - 1, 0, -1):
            if li[i][j] == 1:
                temp_result[1] = (i, j)
                break
        if (temp_result[1][1] - temp_result[0][1] + 1)%2:
            if temp_result[1][1] - temp_result[0][1] + 1 == sum(li[i][temp_result[0][1]:temp_result[1][1] + 1]) and max_value < \
                    temp_result[1][1] - temp_result[0][1] + 1:
                max_value = temp_result[1][1] - temp_result[0][1] + 1
                result = temp_result[:]
        else:
            return False

    if max_value == 1 or max_value == 2:
        return False

    if not result:
        return False

    cnt = 1

    for i in range(len(li)):
        if i < result[0][1] or i > result[1][1]:
            if not sum([x[i] for x in li]) == 0:
                return False
        else:
            if not sum([x[i] for x in li]) == cnt:
                return False
            elif i < (result[0][1] + result[1][1]) // 2:
                cnt += 1
            elif i >= (result[0][1] + result[1][1]) // 2:
                cnt -= 1
    up_tf = True
    for i in range(1, ((result[1][1] - result[0][1]) // 2) + 1):
        if not result[1][1] - result[0][1] + 1 - (2 * i) == sum(li[result[0][0] - i][result[0][1] + i:result[1][1] - i + 1]):
            up_tf = False

    down_tf = True
    if not up_tf:
        for i in range(1, ((result[1][1] - result[0][1]) // 2) + 1):
            if not result[1][1] - result[0][1] + 1 - (2 * i) == sum(li[result[0][0] + i][result[0][1] + i:result[1][1] - i + 1]):
                down_tf = False
    else:
        result[2] = (result[1][0] - ((result[1][1] - result[0][1]) // 2), (result[0][1] + result[1][1]) // 2)
        return True

    if down_tf:
        result[2] = (((result[1][1] - result[0][1]) // 2) + result[1][0], (result[0][1] + result[1][1]) // 2)
        return True
    else:
        return False

def search_sero(li):
    global result
    result = []
    max_value = 0
    for i in range(len(li)):
        temp_result = [(0, 0), (0, 0), (0, 0)]
        for j in range(len(li)):
            if li[j][i] == 1:
                temp_result[0] = (j, i)
                break
        for j in range(len(li) - 1, 0, -1):
            if li[j][i] == 1:
                temp_result[1] = (j, i)
                break
        if (temp_result[1][1] - temp_result[0][1] + 1)%2:
            if temp_result[1][0] - temp_result[0][0] + 1 == sum([li[x][temp_result[0][1]] for x in range(temp_result[0][0], temp_result[1][0] + 1)]) and max_value < \
                    temp_result[1][0] - temp_result[0][0] + 1:
                max_value = temp_result[1][0] - temp_result[0][0] + 1
                result = temp_result[:]
        else:
            return False

    if max_value == 1 or max_value == 2:
        return False

    if not result:
        return False

    cnt = 1

    for i in range(len(li)):
        if i < result[0][0] or i > result[1][0]:
            if not sum(li[i]) == 0:
                return False
        else:
            if not sum(li[i]) == cnt:
                return False
            elif i < (result[0][0] + result[1][0]) // 2:
                cnt += 1
            elif i >= (result[0][0] + result[1][0]) // 2:
                cnt -= 1

    left_tf = True
    for i in range(1, ((result[1][0] - result[0][0]) // 2) + 1):
        if not result[1][0] - result[0][0] + 1 - (2 * i) == sum([x[result[0][1] - i] for x in li[result[0][0] + i:result[1][0] +1 - i]]):
            left_tf = False

    right_tf = True
    if not left_tf:
        for i in range(1, ((result[1][0] - result[0][0]) // 2) + 1):
            if not result[1][0] - result[0][0] + 1 - (2 * i) == sum([x[result[0][1] + i] for x in li[result[0][0] + i:result[1][0] +1 - i]]):
                right_tf = False
    else:
        result[2] = ((result[0][0] + result[1][0]) // 2, result[1][1] - ((result[1][0]- result[0][0]) // 2))
        return True

    if right_tf:
        result[2] = ((result[0][0] + result[1][0]) // 2, ((result[1][0]- result[0][0]) // 2) + result[1][1])
        return True
    else:
        return False


for n in range(10):
    msg = input()
    li.append([int(x) for x in msg])

if search_garo(li):
    result.sort()
    for r in result:
        print(f"{r[0] + 1} {r[1] + 1}")
else:
    if search_sero(li):
        result.sort()
        for r in result:
            print(f"{r[0] + 1} {r[1] + 1}")
    else:
        print(0)