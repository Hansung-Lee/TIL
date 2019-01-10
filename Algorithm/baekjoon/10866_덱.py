N = int(input())

li_deque = []

for n in range(N):
    msg = input()
    command = msg.split()[0]

    if command=='push_front':
        li_deque.insert(0, msg.split()[1])
    elif command=='push_back':
        li_deque.append(msg.split()[1])
    elif command=='pop_front':
        if li_deque:
            print(li_deque[0])
            del li_deque[0]
        else:
            print('-1')
    elif command=='pop_back':
        if li_deque:
            print(li_deque[-1])
            del li_deque[-1]
        else:
            print('-1')
    elif command=='size':
        print(len(li_deque))
    elif command=='empty':
        if li_deque:
            print('0')
        else:
            print('1')
    elif command=='front':
        if li_deque:
            print(li_deque[0])
        else:
            print('-1')
    elif command=='back':
        if li_deque:
            print(li_deque[-1])
        else:
            print('-1')