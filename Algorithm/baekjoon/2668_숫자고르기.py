N = int(input())

li = [[n for n in range(1,N+1)],[]]
for n in range(N):
    li[1].append(int(input()))

tree = [[] for n in range(N+1)]
for n in range(N):
    tree[li[0][n]].append(li[1][n])

result = []

for i in range(1,N+1):
    visited = [False] * (N+1)
    visited[i] = True
    temp_result = [i]
    stack = [i]
    while stack:
        a = stack.pop()
        for t in tree[a]:
            if visited[t] == False:
                stack.append(t)
                temp_result.append(t)
                visited[t] = True
            if i == t:
                result.extend(temp_result)

result = list(set(result))
result.sort()

print(len(result))
for r in result:
    print(r)