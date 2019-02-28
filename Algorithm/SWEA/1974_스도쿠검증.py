def check(li):
    check_li = [0] * 10
    for item in li:
        for x in range(1, 10):
            if item == x:
                if check_li[x] == 1:
                    return False
                check_li[x] = 1
                break
    return True

def main_func():
    # 가로 탐색
    for i in range(9):
        if not check(sudoku[i]):
            return False

    # 행렬 전치
    for i in range(9):
        for j in range(9):
            if i < j:
                sudoku[i][j], sudoku[j][i] = sudoku[j][i], sudoku[i][j]
    
    # 세로 탐색
    for i in range(9):
        if not check(sudoku[i]):
            return False

    # 네모 탐색
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for q in range(3):
                for p in range(3):
                    square.append(sudoku[i + q][j + p])
            if not check(square):
                return False

    return True


T = int(input())

for t in range(T):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    if main_func():
        print(f"#{t + 1} {1}")
    else:
        print(f"#{t + 1} {0}")