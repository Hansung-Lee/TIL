X = int(input())

stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for s in stick:
    if X >= s:
        X = X-s
        cnt += 1
    if X == 0:
        print(cnt)
        break