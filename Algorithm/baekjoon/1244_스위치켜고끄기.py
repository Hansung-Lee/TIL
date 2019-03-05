def change(idx):
    global switch
    if switch[idx]:
        switch[idx] = 0
    else:
        switch[idx] = 1


N = int(input())
switch = list(map(int, input().split()))

S = int(input())
for s in range(S):
    gender, switch_num = map(int, input().split())

    if gender == 1:
        for i in range(1, (N // switch_num) + 1):
            change(i*switch_num-1)
    else:
        for i in range(min(N - switch_num + 1, switch_num)):
            if switch[switch_num + i-1] == switch[switch_num - i-1]:
                if i == min(N - switch_num + 1, switch_num) - 1:
                    for j in range(switch_num - i, switch_num + i + 1):
                        change(j - 1)
                    break
                else:
                    pass
            else:
                for j in range(switch_num - i + 1, switch_num + i):
                    change(j - 1)
                break

for i in range(((len(switch)-1)//20)+1):
    if i == ((len(switch)-1)//20)+1:
        print(' '.join([str(x) for x in switch[20*i:((20*i)+(len(switch)%20))]]))
    else:
        print(' '.join([str(x) for x in switch[20*i:(20*i)+20]]))