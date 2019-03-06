w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
t1 = t
p1, q1 = p, q

now_d = 'right_up'

while t > 0:
    if now_d == 'right_up':
        if t > (w - p) or t > (h - q):
            if (w - p) < (h - q):
                num = (w - p)
                p += num
                q += num
                t -= num
                now_d = 'left_up'

            elif (w - p) > (h - q):
                num = (h - q)
                p += num
                q += num
                t -= num
                now_d = 'right_down'

            else:
                num = (w - p)
                p += num
                q += num
                t -= num
                now_d = 'left_down'
        else:
            num = t
            p += num
            q += num
            t -= num

    elif now_d == 'left_up':
        if t > p or t > (h - q):
            if p < (h - q):
                num = p
                p -= num
                q += num
                t -= num
                now_d = 'right_up'

            elif p > (h - q):
                num = (h - q)
                p -= num
                q += num
                t -= num
                now_d = 'left_down'

            else:
                num = p
                p -= num
                q += num
                t -= num
                now_d = 'right_down'
        else:
            num = t
            p -= num
            q += num
            t -= num

    elif now_d == 'right_down':
        if t > (w - p) or  t > q:
            if (w - p) < q:
                num = (w - p)
                p += num
                q -= num
                t -= num
                now_d = 'left_down'

            elif (w - p) > q:
                num = q
                p += num
                q -= num
                t -= num
                now_d = 'right_up'

            else:
                num = (w - p)
                p += num
                q -= num
                t -= num
                now_d = 'left_up'
        else:
            num = t
            p += num
            q -= num
            t -= num

    elif now_d == 'left_down':
        if t > p or t > q:
            if p < q:
                num = p
                p -= num
                q -= num
                t -= num
                now_d = 'right_down'

            elif p > q:
                num = q
                p -= num
                q -= num
                t -= num
                now_d = 'left_up'

            else:
                num = p
                p -= num
                q -= num
                t -= num
                now_d = 'right_up'
        else:
            num = t
            p -= num
            q -= num
            t -= num

print("{} {}".format(p, q))