def find_set(x):
    global p

    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]


def union(x, y):
    global p

    temp = find_set(y)
    for j in range(1, len(p)):
        if p[j] == temp:
            p[j] = find_set(x)


T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    li_edge = []

    for e in range(E):
        li_edge.append(list(map(int, input().split())))

    li_edge.sort(key=lambda x: x[2])

    p = [x for x in range(V+1)]
    
    result = 0
    cnt = 0

    for i in range(len(li_edge)):
        if find_set(li_edge[i][0]) != find_set(li_edge[i][1]):
            union(li_edge[i][0], li_edge[i][1])
            result += li_edge[i][2]
            cnt += 1
        if cnt == V:
            break

    print("#{} {}".format(t+1, result))