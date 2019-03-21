T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li = []
    code_li = []

    for n in range(N):
        li.append(list(input().strip()))

    for i in range(len(li)):
        if li[i] != ['0']*M and not li[i] in code_li:
            code_li.append(li[i][:])

    end = 0
    code = []
    for m_code_li in code_li:
        for i in range(len(m_code_li)-1, -1, -1):
            if m_code_li[i] != '0':
                end = i
                break
        temp = ''
        for i in range(end, -1, -1):
            if m_code_li[i] == '0':
                if ['0']*(i+1) == m_code_li[:i+1]:
                    code.append(temp[::-1])
                    break
                elif (M//51):
                    if temp and m_code_li[i-1] == '0' and m_code_li[i-2] == '0' and m_code_li[i-3] == '0' and m_code_li[i-4] == '0':
                        code.append(temp[::-1])
                        temp = ''
                    else:
                        temp += m_code_li[i]
                elif not (M//51):
                    if temp and m_code_li[i-1] == '0':
                        code.append(temp[::-1])
                        temp = ''
                    else:
                        temp += m_code_li[i]
            else:
                temp += m_code_li[i]

    code = list(set(code))
    result = 0

    for c in code:
        if len(c) < 14:
            pass
        else:
            num = len(c)//14
            pattern = {
                '0'*num*3 + '1'*num*2 + '0'*num*1 + '1'*num*1: 0,
                '0'*num*2 + '1'*num*2 + '0'*num*2 + '1'*num*1: 1,
                '0'*num*2 + '1'*num*1 + '0'*num*2 + '1'*num*2: 2,
                '0'*num*1 + '1'*num*4 + '0'*num*1 + '1'*num*1: 3,
                '0'*num*1 + '1'*num*1 + '0'*num*3 + '1'*num*2: 4,
                '0'*num*1 + '1'*num*2 + '0'*num*3 + '1'*num*1: 5,
                '0'*num*1 + '1'*num*1 + '0'*num*1 + '1'*num*4: 6,
                '0'*num*1 + '1'*num*3 + '0'*num*1 + '1'*num*2: 7,
                '0'*num*1 + '1'*num*2 + '0'*num*1 + '1'*num*3: 8,
                '0'*num*3 + '1'*num*1 + '0'*num*1 + '1'*num*2: 9
            }
            
            code2 = []

            for m in c:
                temp = ''
                try:
                    n = int(m)
                except:
                    n = ord(m)-55
                for i in range(4):
                    temp += str(n%2)
                    n //= 2
                code2.extend(list(map(int, temp[::-1])))
            
            code3 = []
            start = 0
            for i in range(len(code2)):
                temp = ''.join([str(x) for x in code2[i:i+7*num]])
                if pattern.get(temp) != None:
                    start = i
                    break

            for i in range(start,len(code2),7*num):
                temp = ''.join([str(x) for x in code2[i:i+7*num]])
                code3.append(pattern.get(temp))

            temp_copy = []
            for i in range(len(code3)):
                if code3[i]!=None:
                    temp_copy.append(code3[i])

            code3 = temp_copy[:]

            if len(code3) < 8:
                c = '0'*num + c[:]

                code2 = []

                for m in c:
                    temp = ''
                    try:
                        n = int(m)
                    except:
                        n = ord(m)-55
                    for i in range(4):
                        temp += str(n%2)
                        n //= 2
                    code2.extend(list(map(int, temp[::-1])))
                
                code3 = []
                start = 0
                for i in range(len(code2)):
                    temp = ''.join([str(x) for x in code2[i:i+7*num]])
                    if pattern.get(temp) != None:
                        start = i
                        break

                for i in range(start,len(code2),7*num):
                    temp = ''.join([str(x) for x in code2[i:i+7*num]])
                    code3.append(pattern.get(temp))
                temp_copy = []
                for i in range(len(code3)):
                    if code3[i]!=None:
                        temp_copy.append(code3[i])

                code3 = temp_copy[:]

            num = 0
            for i in range(len(code3)):
                if i == len(code3)-1:
                    num += code3[i]
                elif i % 2:
                    num += code3[i]
                else:
                    num += code3[i]*3

            if not num%10:
                result += sum(code3)
    
    print("#{} {}".format(t+1, result))