import sys
sys.setrecursionlimit(2000)

def dfs(v):
    global result_dfs
    if v in result_dfs:
        pass
    else:
        result_dfs.append(v)
        for k in tree[v]:
            dfs(k)

N, M, V = map(int, input().split())

tree = [[] for x in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for t in tree:
    t.sort()

result_dfs = []
result_bfs = ""

# DFS
dfs(V)

# BFS
visited = [False] * (N+1)
queue = [V]
visited[V] = True

while queue:
    node = queue.pop(0)
    result_bfs += f"{node} "

    for n in tree[node]:
        if visited[n] == False:
            queue.append(n)
            visited[n] = True

print(" ".join([str(x) for x in result_dfs]))
print(result_bfs)