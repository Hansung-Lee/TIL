for t in range(10):
    case_num = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))
    
    sero = 0
    for i in range(100):
        if ladder[99][i] == 2:
            sero = i
            break
    
    for i in range(98, -1, -1):
        if sero == 0:
            if ladder[i][sero+1] == 1:
                sero += 1
            while(ladder[i][sero+1]):
                sero += 1
        elif sero == 99:
            if ladder[i][sero-1] == 1:
                sero -= 1
            while(ladder[i][sero-1]):
                sero -= 1
                if sero == 0:
                    break
        else:
            if ladder[i][sero-1] == 1:
                sero -= 1
                while(ladder[i][sero-1]):
                    sero -= 1
            elif ladder[i][sero+1] == 1:
                sero += 1
                while(ladder[i][sero+1]):
                    sero += 1
                    if sero == 99:
                        break
    
    print(f"#{case_num} {sero}")