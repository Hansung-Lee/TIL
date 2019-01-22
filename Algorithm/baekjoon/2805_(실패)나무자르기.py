N, M = map(int, input().split())
li_H = list(map(int, input().split()))

max_h = max(li_H)
limit = int(max_h//2)
center_h = limit
tf = False

while limit!=0:
    namu = 0
    for h in li_H:
        if h > center_h:
            namu = namu + h - center_h
    if namu > M:
        limit = int(limit//2)
        center_h += limit
        tf = False
    elif namu < M:
        limit = int(limit//2)
        center_h -= limit
        tf = True
    else:
        break

if tf:
    print(center_h-1)
else:
    print(center_h)