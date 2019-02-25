for t in range(10):
    N, S = map(int, input().split())
    tree = [[] for x in range(N + 1)]

    li = list(map(int, input().split()))

    for i in range(0, len(li), 2):
        tree[li[i]].append(li[i + 1])

    visited = [False] * (N + 1)

    # queue = [[level, node]]
    queue = [[1, S]]
    visited[S] = True
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)

        for k in tree[node[1]]:
            if not visited[k]:
                queue.append([node[0] + 1, k])
                visited[k] = True

    result.sort()

    print(f"#{t + 1} {result[-1][1]}")