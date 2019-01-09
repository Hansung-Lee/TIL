T = int(input())

for t in range(T):
    li = [i for i in input()]
    cnt_left = 0  # (의 개수를 센다
    cnt_right = 0 # )의 개수를 센다
    breaker = True

    for l in li:
        if cnt_right>cnt_left:
            print('NO')
            breaker = False
            break
        
        else:
            if l=='(':
                cnt_left +=1
            else:
                cnt_right +=1
                
    if breaker:
        if cnt_left==cnt_right:
            print('YES')
        else:
            print('NO')