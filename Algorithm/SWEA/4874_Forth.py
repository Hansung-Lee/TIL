T = int(input())

for t in range(T):
    postfix = input().split()

    stack = []
    operator_cnt = 0
    num_cnt = 0

    try:
        for pf in postfix:
            if pf == '+':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a+b))
            elif pf == '-':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a-b))
            elif pf == '*':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a*b))
            elif pf == '/':
                operator_cnt += 1
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a//b))
            elif pf == '.':
                if (num_cnt - operator_cnt) == 1:
                    print(f"#{t+1} {stack.pop()}")
                else:
                    print(f"#{t+1} error")
            else:
                num_cnt += 1
                stack.append(pf)
    except:
        print(f"#{t+1} error")