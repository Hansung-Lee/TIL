T = int(input())
for t in range(T):
    P, Pa, Pb = map(int, input().split())

    a_tf = False  # A의 페이지 검색 성공/실패
    b_tf = False  # B의 페이지 검색 성공/실패
    a_cnt = 0  # A의 탐색 횟수
    b_cnt = 0  # B의 탐색 횟수

    # A의 이진탐색
    l = 1
    r = P
    while l <= r:
        c = (l + r) // 2
        a_cnt += 1
        if c == Pa:  # 검색 성공
            a_tf = True
            break
        elif c > Pa:
            r = c
        else:
            l = c

    # B의 이진탐색
    l = 1
    r = P
    while l <= r:
        b_cnt += 1
        c = (l + r) // 2
        if c == Pb:  # 검색 성공
            b_tf = True
            break
        elif c > Pb:
            r = c
        else:
            l = c

    result = '0'
    if a_tf and b_tf:
        if a_cnt > b_cnt:
            result = 'B'
        elif a_cnt < b_cnt:
            result = 'A'
        else:
            result = '0'
    elif a_tf:
        result = 'A'
    elif b_tf:
        result = 'B'

    print(f"#{t+1} {result}")