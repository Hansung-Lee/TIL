def push(node, num):
    global tree
    tree[node][0] = num

    parent_node = node // 2
    left_tf = False

    while parent_node:
        if tree[node][0] > tree[parent_node][0]:
            if not tree[parent_node][1] or left_tf:
                tree[parent_node][1] = node
                left_tf = False
                break
            else:
                tree[parent_node][2] = node
                break
        else:
            tree[node][0], tree[parent_node][0] = tree[parent_node][0], tree[node][0]
            if not tree[parent_node][1]:
                tree[parent_node][1] = node
                node = parent_node
                parent_node = node // 2
                left_tf = True
            else:
                tree[parent_node][2] = node
                node = parent_node
                parent_node = node // 2


T = int(input())

for t in range(T):
    N = int(input())
    li_push = list(map(int, input().split()))

    tree = [[0] * 3 for _ in range(N + 1)]

    for i in range(len(li_push)):
        push(i + 1, li_push[i])

    node = (N // 2)
    result = 0

    while node:
        result += tree[node][0]
        node //= 2

    print("#{} {}".format(t + 1, result))