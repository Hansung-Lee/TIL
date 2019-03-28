T = int(input())

for t in range(T):
    stations = list(map(int, input().split()))
    N = stations.pop(0)

    tree = [[] for _ in range(N+1)]
    result = 0
    breaker = False

    for i in range(1,N):
        for j in range(stations[i-1],0,-1):
            tree[i].append(j+i)
            if j+i == N:
                breaker = True
                break
            elif j+i > N:
                tree[i].remove(j+i)
                tree[i].append(N)
                breaker = True
                break
        if breaker:
            break

    queue = [[1,0]]
    check = []

    while queue:
        bus = queue.pop(0)

        if bus[0] == N:
            result = bus[1]-1
            break

        for i in range(len(tree[bus[0]])):
            if not tree[bus[0]][i] in check:
                check.append(tree[bus[0]][i])
                queue.append([tree[bus[0]][i], bus[1]+1])

    print("#{} {}".format(t+1, result))