def perm(n):
    global li_perm
    global min_value, temp

    if n == 0:         
        if min_value > temp:
            min_value = temp
        return

    for i in range(N):
        if not i in li_perm:
            li_perm.append(i)
            temp += (li[li_perm[-1]][len(li_perm)-1])
            if temp < min_value:
                perm(n-1)
            temp -= (li[li_perm[-1]][len(li_perm)-1])
            li_perm.remove(i)


T = int(input())

for t in range(T):
    N = int(input())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))
    
    li_perm = []
    min_value = 9999
    temp = 0
    perm(N)

    print("#{} {}".format(t+1, min_value))