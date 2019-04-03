T = int(input())

for t in range(T):
    prices = list(map(int, input().split()))
    months = list(map(int, input().split()))
    result = [0]*12

    for i in range(12):
        result[i] = months[i]*prices[0]
        if result[i] > prices[1]:
            result[i] = prices[1]

    temp = result[::-1]

    for i in range(12):
        if result[i]:
            if i == 11:
                if result[i]>prices[2]:
                    result[i] = prices[2]
            elif i == 10:
                if result[i]+result[i+1]>prices[2]:
                    result[i] = prices[2]
                    result[i+1] = 0
            else:
                if result[i]+result[i+1]+result[i+2]>prices[2]:
                    result[i] = prices[2]
                    result[i+1] = 0
                    result[i+2] = 0
    
    for i in range(12):
        if temp[i]:
            if i == 11:
                if temp[i]>prices[2]:
                    temp[i] = prices[2]
            elif i == 10:
                if temp[i]+temp[i+1]>prices[2]:
                    temp[i] = prices[2]
                    temp[i+1] = 0
            else:
                if temp[i]+temp[i+1]+temp[i+2]>prices[2]:
                    temp[i] = prices[2]
                    temp[i+1] = 0
                    temp[i+2] = 0
    
    if sum(temp)<sum(result):
        result = temp[:]

    
    if sum(result) < prices[3]:
        print("#{} {}".format(t+1, sum(result)))
    else:
        print("#{} {}".format(t+1, prices[3]))