def binarySearch(li, k):
    l = 0
    r = len(li)-1
    direction = 0 # 1: 왼쪽, 2: 오른쪽
    q = 0

    while l <= r:
        q += 1
        m = (l+r)//2

        if li[m] == k:
            return 1
        elif li[m] > k:
            if direction == 1:
                return 0
            direction = 1
            r = m - 1
        else:
            if direction == 2:
                return 0
            direction = 2
            l = m + 1

    return 0


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li_N = list(map(int, input().split()))
    li_M = list(map(int, input().split()))

    li_N.sort()

    cnt = 0

    for i in range(len(li_M)):
        cnt += binarySearch(li_N, li_M[i])

    print("#{} {}".format(t+1, cnt))