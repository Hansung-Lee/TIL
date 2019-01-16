import sys
T = int(sys.stdin.readline())

for t in range(T):
    N, K = map(int, sys.stdin.readline().split())
    li_D = list(map(int, sys.stdin.readline().split()))
    
    li_graph = [[] for i in range(N)]
    for k in range(K):
        a, b = map(int, sys.stdin.readline().split())
        li_graph[b-1].append(a)

    W = int(sys.stdin.readline())


    print(li_graph)