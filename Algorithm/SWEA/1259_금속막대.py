T = int(input())

for t in range(T):
    n = int(input())
    temp_N = list(map(int, input().split()))
    li_N = []

    for i in range(n):
        li_N.append([temp_N[2 * i], temp_N[2 * i + 1]])

    temp_result = []
    result = []

    tf = True

    for i in range(len(li_N)):
        temp_result.append(li_N[i][:])
        while True:
            for j in range(len(li_N)):
                if temp_result[-1][1] == li_N[j][0]:
                    temp_result.append(li_N[j][:])
                    tf = False
                if j == len(li_N) - 1:
                    if not tf:
                        tf = True
                    else:
                        tf = False
            if not tf:
                break
        if len(result) <= len(temp_result):
            result = temp_result[:]
        temp_result.clear()

    str_ = ''
    for s in result:
        str_ += str(s[0]) + ' ' + str(s[1]) + ' '

    print(f"#{t + 1} {str_}")