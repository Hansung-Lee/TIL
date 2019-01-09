N, M, V = map(int, input().split())

li_M = []
dict_N = {}

for n in range(N):
    dict_N[n+1]=True

for m in range(M):
    msg = input().split()
    li_M.append(list(map(int, msg)))
    li_M.append(list(map(int, msg))[::-1])

def dfs(dict_N, li_M, V):
    for n in range(len(dict_N)):
        dict_N[V] = False



def bfs(dict_N, li_M, V):
    #While():
        dict_N[V] = False
        for m in li_M:
            if V == m[0]:
                print(m[1],end =' ')


dfs(dict_N, li_M, V)
bfs(dict_N, li_M, V)