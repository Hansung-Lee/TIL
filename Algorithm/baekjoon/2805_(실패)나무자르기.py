N, M = map(int, input().split())
li_H = list(map(int, input().split()))

start = 0
end = max(li_H)
center = 0
tf = False

while start<=end:
    namu = 0
    center=(start+end)//2
    for h in li_H:
        if h > center:
            namu = namu + h - center
    if namu > M:
        start=center+1
        tf = False
    elif namu < M:
        end=center-1
        tf = True
    else:
        tf = False
        break

if tf:
    print(center-1)
else:
    print(center)