T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    A = int((((x2-x1)**2)+((y2-y1)**2))**0.5)
    B = r1+r2

    if A==B or A==abs(r1-r2):
        print(1)
    elif A>B or A<abs(r1-r2):
        print(0)
    else:
        print(2)