E, S, M = map(int, input().split())

li = []
e = s = m = 1

for i in range(7980):
    li.append([e, s, m])
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

print(li.index([E,S,M])+1)