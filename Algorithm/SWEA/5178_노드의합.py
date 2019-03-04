T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())

    tree = [0 for _ in range(N + 1)]

    for m in range(M):
        a, b = map(int, input().split())
        tree[a] = b

    for i in range(N, 0, -1):
        tree[(i // 2)] += tree[i]

    print("#{} {}".format(t + 1, tree[L]))