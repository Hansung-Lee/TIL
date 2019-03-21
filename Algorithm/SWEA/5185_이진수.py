T = int(input())

for t in range(T):
    msg = input().split()[1]

    li = []

    for m in msg:
        temp = ''
        try:
            n = int(m)
        except:
            n = ord(m)-55
        for i in range(4):
            temp += str(n%2)
            n //= 2
        li.extend(list(map(int, temp[::-1])))
    
    print("#{} {}".format(t+1, ''.join(list(map(str,li)))))