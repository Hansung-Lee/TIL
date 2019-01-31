T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li_N = []
    result_li = []

    for n in range(N):
        msg = input()
        li_N.append([x for x in msg])
    
    row_search_tf = True

    # 가로 탐색 (row, 행)
    for i in range(len(li_N)):
        for j in range(len(li_N[i])-M+1):
            temp_li = []
            search_tf = True
            for z in range(M+j-1,j-1,-1):
                temp_li.append(li_N[i][z])
            for y in range(j,M+j):
                if li_N[i][y] != temp_li[y-j]:
                    search_tf = False
                    break
            if search_tf:
                result_li = temp_li
                break
        if search_tf:
            break
        if i == len(li_N)-1:
            row_search_tf = False
    
    # 가로 탐색 실패시 세로 탐색 실행
    if not row_search_tf:
        # 세로 탐색 (column, 열)
        for i in range(len(li_N[0])):
            for j in range(len(li_N)-M+1):
                temp_li = []
                search_tf = True
                for z in range(M+j-1,j-1,-1):
                    temp_li.append(li_N[z][i])
                for y in range(j,M+j):
                    if li_N[y][i] != temp_li[y-j]:
                        search_tf = False
                        break
                if search_tf:
                    result_li = temp_li
                    break
            if search_tf:
                break

    result = ''
    for rst in result_li:
        result += rst

    print(f"#{t+1} {result}")