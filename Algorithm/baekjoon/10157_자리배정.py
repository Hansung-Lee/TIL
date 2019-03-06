C, R = map(int, input().split())
K = int(input())

li = ["0 0"]

x = y = 1
limit_C = [2,C]
limit_R = [1,R]
now_d = 'up'

for i in range(C*R):
    if now_d == 'up':
        li.append("{} {}".format(x,y))
        y += 1
        if y > limit_R[1]:
            y -= 1
            x += 1
            limit_R[1] -= 1
            now_d = 'right'
    elif now_d == 'right':
        li.append("{} {}".format(x,y))
        x += 1
        if x > limit_C[1]:
            x -= 1
            y -= 1
            limit_C[1] -= 1
            now_d = 'down'
    elif now_d == 'down':
        li.append("{} {}".format(x,y))
        y -= 1
        if y < limit_R[0]:
            y += 1
            x -= 1
            limit_R[0] += 1
            now_d = 'left'
    elif now_d == 'left':
        li.append("{} {}".format(x,y))
        x -= 1
        if x < limit_C[0]:
            x += 1
            y += 1
            limit_C[0] += 1
            now_d = 'up'
if K <= C*R:
    print(li[K])
else:
    print(0)