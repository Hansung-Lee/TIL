N, M = map(int, input().split())
li = []
for i in range(1<<N+1):
    result = []
    for j in range(N+1):
        if i & (1<<j):
            if j:
                result.append(j)
    if len(result) == M:
        li.append(' '.join([str(x) for x in result]))

li = list(set(li))
li.sort()
for l in li:
    print(l)