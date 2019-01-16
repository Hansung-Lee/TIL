case_num = 1
for t in range(10):
    N = int(input())
    li_N = list(map(int, input().split()))
    okview = 0

    li_apart = []

    for n in li_N:
        temp_apart = []
        for j in range(n):
            temp_apart.append(1)
        for j in range(max(li_N)-n):
            temp_apart.append(0)
        li_apart.append(temp_apart)

    for i in range(2,len(li_apart)-2):
        for j in range(len(li_apart[i])):
            if li_apart[i][j] == 1:
                if li_apart[i+1][j] == 0 and li_apart[i+2][j] == 0 \
                and li_apart[i-1][j] == 0 and li_apart[i-2][j] == 0:
                    okview += 1

    print(f'#{case_num} {okview}')
    case_num += 1