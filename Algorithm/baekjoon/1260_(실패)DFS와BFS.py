N, M, V = map(int, input().split())

li_M = []

for m in range(M):
    msg = input().split()
    li_M.append(list(map(int, msg)))
    li_M.append(list(map(int, msg))[::-1])

def dfs(li_M, V):
    visited = [True for n in range(N)]

    li_dfs = [V]
    while_breaker = True
    while(while_breaker):
        if visited[V-1]:
            visited[V-1] = False
            for m in li_M:
                if V == m[0] and visited[m[1]-1]:
                    li_dfs.append(m[1])
                    visited[m[1]-1] = False
                    V = m[1]
        for idx, v in enumerate(visited):
            if v:
                V=idx
                break
            if idx==len(visited)-1:
                while_breaker = False
    return li_dfs
        
def bfs(li_M, V):
    visited = [True for n in range(N)]

    li_bfs = [V]
    while_breaker = True
    while(while_breaker):
        if visited[V-1]:
            visited[V-1] = False
            for m in li_M:
                if V == m[0] and visited[m[1]-1]:
                    li_bfs.append(m[1])
                    visited[m[1]-1] = False
        for idx, v in enumerate(visited):
            if v:
                V=idx
                break
            if idx==len(visited)-1:
                while_breaker = False
    return li_bfs

print(dfs(li_M, V))
print(bfs(li_M, V))