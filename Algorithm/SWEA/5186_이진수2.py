T = int(input())

for t in range(T):
    num = float(input())
    msg = str(num)[2:]
    
    result = ''

    for i in range(1,13):
        if num >= 2**(-i):
            num -= 2**(-i)
            result += '1'
        else:
            result += '0'
        if num == 0:
            break
    if num:
        result = 'overflow'
    
    print("#{} {}".format(t+1, result))