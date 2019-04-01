def bfs():
    global queue, visited

    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            if i == 0:
                if x+1 == M:
                    return y+1
                elif x+1 not in visited and x+1 <= 1000000:
                    queue.append((x+1, y+1))
                    visited.append(x+1)
            elif i == 1:
                if x-1 == M:
                    return y+1
                elif x-1 not in visited and x-1 > 0:
                    queue.append((x-1, y+1))
                    visited.append(x-1)
            elif i == 2:
                if x*2 == M:
                    return y+1
                elif x*2 not in visited and x*2 <= 1000000:
                    queue.append((x*2, y+1))
                    visited.append(x*2)
            elif i == 3:
                if x-10 == M:
                    return y+1
                elif x-10 not in visited and x-10 > 0:
                    queue.append((x-10, y+1))
                    visited.append(x-10)


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    
    queue = [(N, 0)]
    visited = [N]

    print("#{} {}".format(t+1, bfs()))