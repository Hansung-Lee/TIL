T = int(input())

for t in range(T):
    input_ = input().split()
    N = int(input_[0])
    S = input_[1]

    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))
    
    answer = []

    if S == 'up':
        result = []

        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(li[j][i])
            result.append(temp)
        
        for i in range(len(result)):
            cnt = 0
            for j in range(len(result[i])-1):
                if cnt:
                    cnt -= 1
                else:
                    for q in range(j+1,len(result[i])):
                        cnt += 1
                        if result[i][j] == result[i][q]:
                            result[i][j] *= 2
                            result[i][q] = 0
                            break
                        elif result[i][q]:
                            cnt = 0
                            break
            temp = []
            for j in range(len(result[i])):
                if result[i][j]:
                    temp.append(result[i][j])
            
            for j in range(len(result[i])-len(temp)):
                temp.append(0)
            
            answer.append(temp[:])
    
        for i in range(len(answer)):
            for j in range(len(answer[0])):
                if i < j:
                    answer[i][j], answer[j][i] = answer[j][i], answer[i][j]
    
    elif S == 'down':
        result = []

        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(li[j][i])
            result.append(temp)
        
        for i in range(len(result)):
            cnt = 0
            for j in range(len(result[i])-1, 0, -1):
                if cnt:
                    cnt -= 1
                else:
                    for q in range(j-1, -1, -1):
                        cnt += 1
                        if result[i][j] == result[i][q]:
                            result[i][j] *= 2
                            result[i][q] = 0
                            break
                        elif result[i][q]:
                            cnt = 0
                            break
            temp = []
            for j in range(len(result[i])):
                if result[i][j]:
                    temp.append(result[i][j])
            
            for j in range(len(result[i])-len(temp)):
                temp.insert(0, 0)
            
            answer.append(temp[:])
    
        for i in range(len(answer)):
            for j in range(len(answer[0])):
                if i < j:
                    answer[i][j], answer[j][i] = answer[j][i], answer[i][j]

    elif S == 'right':
        for i in range(len(li)):
            cnt = 0
            for j in range(len(li[i])-1, 0, -1):
                if cnt:
                    cnt -= 1
                else:
                    for q in range(j-1, -1, -1):
                        cnt += 1
                        if li[i][j] == li[i][q]:
                            li[i][j] *= 2
                            li[i][q] = 0
                            break
                        elif li[i][q]:
                            cnt = 0
                            break
            temp = []
            for j in range(len(li[i])):
                if li[i][j]:
                    temp.append(li[i][j])
            
            for j in range(len(li[i])-len(temp)):
                temp.insert(0, 0)
            
            answer.append(temp[:])

    elif S == 'left':
        for i in range(len(li)):
            cnt = 0
            for j in range(len(li[i])-1):
                if cnt:
                    cnt -= 1
                else:
                    for q in range(j+1,len(li[i])):
                        cnt += 1
                        if li[i][j] == li[i][q]:
                            li[i][j] *= 2
                            li[i][q] = 0
                            break
                        elif li[i][q]:
                            cnt = 0
                            break
            temp = []
            for j in range(len(li[i])):
                if li[i][j]:
                    temp.append(li[i][j])
            
            for j in range(len(li[i])-len(temp)):
                temp.append(0)
            
            answer.append(temp[:])

    print("#{}".format(t+1))
    for a in answer:
        print(' '.join(map(str, a)))