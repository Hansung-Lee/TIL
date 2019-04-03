import itertools

T = int(input())

for t in range(T):
    N = int(input())
    li_op = list(map(int, input().split()))
    operators = []
    for i in range(4):
        if i == 0:
            operators.extend(['+']*li_op[i])
        elif i == 1:
            operators.extend(['-']*li_op[i])
        elif i == 2:
            operators.extend(['*']*li_op[i])
        elif i == 3:
            operators.extend(['/']*li_op[i])

    li_nums = list(map(int, input().split()))

    li_perm = list(set(itertools.permutations(operators)))

    min_value = 100000001
    max_value = -100000001

    for i in range(len(li_perm)):
        temp = li_nums[0]
        for j in range(N-1):
            if li_perm[i][j] == '+':
                temp += li_nums[j+1]
            elif li_perm[i][j] == '-':
                temp -= li_nums[j+1]
            elif li_perm[i][j] == '*':
                temp *= li_nums[j+1]
            elif li_perm[i][j] == '/':
                temp = int(temp/li_nums[j+1])

        if min_value > temp:
            min_value = temp
        if max_value < temp:
            max_value = temp

    print("#{} {}".format(t+1, max_value-min_value))