import sys
N, M = map(int, sys.stdin.readline().split())

li = []

for m in range(M):
    a, b = map(int, sys.stdin.readline().split())

    if a in li:
        li.insert(li.index(a), b)
    elif b in li:
        li.insert(li.index(b)-1, a)
    else:
        li.append(a)
        li.append(b)

for i in range(len(li)):
    if i != len(li):
        print(li[i], end=" ")
    else:
        print(li[i])