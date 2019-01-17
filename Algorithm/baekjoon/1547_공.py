M = int(input())
li_change = []

for m in range(M):
    li_change.append(list(map(int, input().split())))
    
now = 1

for change in li_change:
    if now ==1:
        if 1 in change and 2 in change:
            now = 2
        elif 1 in change and 3 in change:
            now = 3
    elif now ==2:
        if 1 in change and 2 in change:
            now = 1
        elif 2 in change and 3 in change:
            now = 3
    elif now ==3:
        if 1 in change and 3 in change:
            now = 1
        elif 2 in change and 3 in change:
            now = 2
print(now)