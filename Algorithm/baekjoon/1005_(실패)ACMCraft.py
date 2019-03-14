import sys

T = int(sys.stdin.readline())

for t in range(T):
    N, K = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(N+1)]

    time = list(map(int, sys.stdin.readline().split()))

    for k in range(K):
        a, b = map(int, sys.stdin.readline().split())
        tree[b].append(a)

    out_degree = [0] * (N+1)

    for i in range(len(tree)):
        for j in tree[i]:
            out_degree[j] += 1

    W = int(sys.stdin.readline())

    queue = [(W,1)]
    dp = [-1] * (N+1)

    while queue:
        node_v = queue.pop(0)
        node_k = []

        for k in tree[node_v[0]]:
            out_degree[k] -= 1
            dp[node_v[1]] = max(dp[node_v[1]], time[k-1])
            
            if out_degree[k] == 0:
                queue.append((k, node_v[1]+1))
    
    result = time[W-1]

    print(result)
    