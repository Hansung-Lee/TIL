T = int(input())

for t in range(T):
    N = int(input())
    li_N = list(map(int, input().split()))

    max_value = 0
    min_value = 1000001

    for n in li_N:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n

    print(f"#{t+1} {max_value-min_value}")