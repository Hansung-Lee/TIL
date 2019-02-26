N, robot_A, robot_B = map(int, input().split())

tree = [[] for n in range(N+1)]
visited = [False] * (N+1)

for n in range(N-1):
    room_A, room_B, length = map(int, input().split())
    tree[room_A].append([room_B, length])
    tree[room_B].append([room_A, length])

stack = [[robot_A, 1]]
visited[robot_A] = True
result = []

while stack:
    room = stack.pop()
    result.append(room)

    if room[0] == robot_B:
        break

    for r in tree[room[0]]:
        if visited[r[0]] == False:
            stack.append([r[0], room[1]+1])
            visited[r[0]] = True

way = []
length = []

for r in result:
    if r[1] < result[-1][1]:
        way.append(r[0])

way.append(result[-1][0])

for i in range(len(way)-1):
    for j in range(len(tree[way[i]])):
        if tree[way[i]][j][0] == way[i+1]:
            length.append(tree[way[i]][j][1])
            break

min_value = 999999

for i in range(len(length)):
    if min_value > (sum(length[:i]) + sum(length[i+1:])):
        min_value = (sum(length[:i]) + sum(length[i+1:]))

print(min_value)