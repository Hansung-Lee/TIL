root = [0, 1, 2, 2]
for i in range(1,9):
    for j in range(2**i):
        root.append(root[-1]+1)
    for j in range(2**i):
        root.append(root[-1])

n2 = [0, 0]
for i in range(1,10):
    for j in range(2**i):
        n2.append(2 + 4*(j//2))

T = int(input())

for t in range(T):
    N = int(input())
    print("#{} {} {}".format(t+1, root[N], n2[N]))