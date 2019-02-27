def bfs(S):
    result_bfs = 0
    visited = [False] * (N+1)

    queue = [[S, 0]]
    visited[S] = True

    while queue:
        node = queue.pop(0)

        if node[1] > result_bfs:
            result_bfs = node[1]

        for k in li[node[0]]:
            if not visited[k]:
                queue.append([k, node[1]+1])
                visited[k] = True
    
    return result_bfs


N = int(input())

li = [[] for x in range(N+1)]

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break
    
    li[a].append(b)
    li[b].append(a)

li_score = [100] * (N+1)

for i in range(1, N+1):
    li_score[i] = bfs(i)


min_value = 100
result = []

for i in range(1, N+1):
    if li_score[i] < min_value:
        min_value = li_score[i]
        result.clear()
        result.append(i)
    elif li_score[i] == min_value:
        result.append(i)

print(f"{min_value} {len(result)}")
print(" ".join([str(x) for x in result]))