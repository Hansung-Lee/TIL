def paint_garo(idx):
    global li
    for i in range(idx, S):
        for j in range(G):
            li[i][j] += 1

def paint_sero(idx):
    global li
    for i in range(S):
        for j in range(idx, G):
            li[i][j] += 1000


G, S = map(int, input().split())
N = int(input())

li = [[0]*G for _ in range(S)]

for n in range(N):
    gs, idx = map(int, input().split())

    if gs == 0:
        paint_garo(idx)
    else:
        paint_sero(idx)

visitied = [[False]*G for _ in range(S)]

result = [0] * (max(max(li))+1)

for i in range(S):
    for j in range(G):
        result[li[i][j]] += 1
print(max(result))