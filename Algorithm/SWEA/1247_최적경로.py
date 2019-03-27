def perm(n):
    global li_perm
    global result, distance

    if n == 0:
        distance += abs(li_perm[-1][0]-E[0])+abs(li_perm[-1][1]-E[1])
        if result > distance:
            result = distance
        distance -= abs(li_perm[-1][0]-E[0])+abs(li_perm[-1][1]-E[1])
        return
    
    for i in range(N):
        customer = [li[2*i], li[2*i+1]]
        if not customer in li_perm:
            li_perm.append(customer)
            distance += abs(li_perm[-1][0]-li_perm[-2][0])+abs(li_perm[-1][1]-li_perm[-2][1])
            if distance < result:
                perm(n-1)
            distance -= abs(li_perm[-1][0]-li_perm[-2][0])+abs(li_perm[-1][1]-li_perm[-2][1])
            li_perm.remove(customer)


T = int(input())

for t in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    S = [li.pop(0), li.pop(0)]
    E = [li.pop(0), li.pop(0)]

    li_perm = [S]
    result = 9999
    distance = 0
    now = S
    
    perm(N)

    print("#{} {}".format(t+1, result))