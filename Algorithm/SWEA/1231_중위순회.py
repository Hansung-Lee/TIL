def inorder(T):
    global result
    if T:
        inorder(tree[T][1])
        result += tree[T][0]
        inorder(tree[T][2])

for t in range(10):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]

    for n in range(N):
        input_ = input().split()
        idx = int(input_[0])
        tree[idx][0] = input_[1]

        if len(input_) == 3:
            tree[idx][1] = int(input_[2])
        elif len(input_) == 4:
            tree[idx][1] = int(input_[2])
            tree[idx][2] = int(input_[3])
    
    result = ''
    inorder(1)

    print("#{} {}".format(t+1, result))