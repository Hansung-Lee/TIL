def check():
    if (x1,y1) == (p2,q2) or \
        (x2,y2) == (p1,q1) or \
        (x1,q1) == (p2,y2) or \
        (x2,q2) == (p1,y1):
        return 'c'
    elif (p1 == x2 and y1 <= q2 <= q1) or (p1 == x2 and y1 <= y2 <= q1) or \
        (x1 == p2 and y1 <= q2 <= q1) or (x1 == p2 and y1 <= y2 <= q1) or \
        (p1 == x2 and y2 <= q1 <= q2) or (p1 == x2 and y2 <= y1 <= q2) or \
        (x1 == p2 and y2 <= q1 <= q2) or (x1 == p2 and y2 <= y1 <= q2) or \
        (y1 == q2 and x1 <= x2 <= p1) or (y1 == q2 and x1 <= p2 <= p1) or \
        (q1 == y2 and x1 <= x2 <= p1) or (q1 == y2 and x1 <= p2 <= p1) or \
        (y1 == q2 and x2 <= x1 <= p2) or (y1 == q2 and x2 <= p1 <= p2) or \
        (q1 == y2 and x2 <= x1 <= p2) or (q1 == y2 and x2 <= p1 <= p2):
        return 'b'
    elif (x1 <= x2 <= p1 and y1 <= y2 <= q1) or \
        (x1 <= x2 <= p1 and y1 <= q2 <= q1) or \
        (x1 <= p2 <= p1 and y1 <= q2 <= q1) or \
        (x1 <= p2 <= p1 and y1 <= y2 <= q1) or \
        (x1 <= x2 <= p1 and x1 <= p2 <= p1 and y2 <= y1 <= q2) or \
        (x1 <= x2 <= p1 and x1 <= p2 <= p1 and y2 <= q1 <= q2) or \
        (y1 <= y2 <= q1 and y1 <= q2 <= q1 and x2 <= x1 <= p2) or \
        (y1 <= y2 <= q1 and y1 <= q2 <= q1 and x2 <= p1 <= p2) or \
        (x2 <= x1 <= p2 and x2 <= p1 <= p2 and y1 <= y2 <= q1) or \
        (x2 <= x1 <= p2 and x2 <= p1 <= p2 and y1 <= q2 <= q1) or \
        (y2 <= y1 <= q2 and y2 <= q1 <= q2 and x1 <= x2 <= p1) or \
        (y2 <= y1 <= q2 and y2 <= q1 <= q2 and x1 <= p2 <= p1) or \
        (x1 <= x2 <= p1 and x1 <= p2 <= p1 and y1 <= y2 <= q1 and y1 <= q2 <= q1) or \
        (x2 <= x1 <= p2 and x2 <= p1 <= p2 and y2 <= y1 <= q2 and y2 <= q1 <= q2):
        return 'a'
    else:
        return 'd'


for t in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    print(check())