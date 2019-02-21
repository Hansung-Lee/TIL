for t in range(10):
    n = int(input())
    expression = input()
    
    # 중위 표기법에서 후위 표기법으로의 변환 알고리즘 (stack 사용)
    # operator = [['operator', in-stack priority, in-coming priority]]
    operator = [['+', 1, 1],['-', 1, 1],['*', 2, 2],['/', 2, 2],['(', 0, 3],[')', -1, -1]]
    stack = [0] * n
    top = -1
    postfix = ''

    for e in expression:
        is_operator = False
        if e == ')':
            is_operator = True
            while True:
                while_breaker = False
                for top_op in operator:
                    if stack[top] == top_op[0]:
                        if top_op[0] == '(':
                            while_breaker = True
                            top -= 1
                            break
                        else:
                            postfix += stack[top]
                            top -= 1
                            break
                if while_breaker:
                    break
        else:
            for op in operator:
                if e == op[0]:
                    is_operator = True
                    while True:
                        while_breaker = False
                        for top_op in operator:
                            if top == -1:
                                top += 1
                                stack[top] = e
                                while_breaker = True
                                break
                            else:
                                if stack[top] == top_op[0]:
                                    if top_op[1] < op[2]:
                                        top += 1
                                        stack[top] = e
                                        while_breaker = True
                                        break
                                    else:
                                        postfix += stack[top]
                                        top -= 1
                                        break
                        if while_breaker:
                            break
                        
        if not is_operator:
            postfix += e

    # 후위 표기법의 수식을 스택을 이용하여 계산
    stack = [0] * len(postfix)
    top = -1
    
    for pf in postfix:
        is_operator = False
        for op in operator:
            if pf == op[0]:
                is_operator = True
                b = int(stack[top])
                top -= 1
                a = int(stack[top])

                if pf == '+':
                    result = a + b
                elif pf == '-':
                    result = a - b
                elif pf == '*':
                    result = a * b
                elif pf == '/':
                    result = a // b

                stack[top] = str(result)
                break

        if not is_operator:
            top += 1
            stack[top] = pf
    print(f"#{t+1} {stack[top]}")