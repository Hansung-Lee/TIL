N = int(input())

li_stack = []

for n in range(N):
    msg = input()
    command = msg.split()[0]

    if command=='push':
        li_stack.append(msg.split()[1])
    elif command=='pop':
        if li_stack:
            print(li_stack[-1])
            del li_stack[-1]
        else:
            print('-1')
    elif command=='size':
        print(len(li_stack))
    elif command=='empty':
        if li_stack:
            print('0')
        else:
            print('1')
    elif command=='top':
        if li_stack:
            print(li_stack[-1])
        else:
            print('-1')
