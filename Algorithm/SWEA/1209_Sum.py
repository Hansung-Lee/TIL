for t in range(10):
    N = int(input())
    li = []
    for i in range(100):
        li.append(list(map(int,input().split())))

    max_value = 0

    # 행의 합 비교
    for i in li:
        value = 0
        for num in i:
            value += num
        if max_value<value:
            max_value = value

    # 리스트 전치
    for i in range(len(li)):
        for j in range(len(li)):
            if i < j:
                li[i][j], li[j][i] = li[j][i], li[i][j]
    # 행의 합 비교 (원본 리스트의 열의 합 비교)
    for i in li:
        value = 0
        for num in i:
            value += num
        if max_value < value:
            max_value = value

    # 대각선 아래 방향
    value = 0
    for i in range(len(li)):
        value += li[i][i]
    if max_value < value:
        max_value = value

    # 대각선 위 방향
    value = 0
    for i in range(len(li)):
        value += li[i][len(li)-1-i]
    if max_value < value:
        max_value = value

    print(f"#{t+1} {max_value}")