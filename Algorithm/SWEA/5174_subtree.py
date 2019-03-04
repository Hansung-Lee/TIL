def check_node(node):
    global result
    if node:
        check_node(tree[node][0])
        check_node(tree[node][1])
        result += 1


T = int(input())

for t in range(T):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = [[0]*2 for _ in range(E+2)]

    for i in range(0, len(edges), 2):
        if not tree[edges[i]][0]:
            tree[edges[i]][0] = edges[i+1]
        else:
            tree[edges[i]][1] = edges[i+1]

    result = 0
    check_node(N)

    print("#{} {}".format(t+1, result))