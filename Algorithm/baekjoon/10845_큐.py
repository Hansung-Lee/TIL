N = int(input())

li_queue = []

for n in range(N):
    msg = input()
    command = msg.split()[0]

    if command=='push':
        li_queue.append(msg.split()[1])
    elif command=='pop':
        if li_queue:
            print(li_queue[0])
            del li_queue[0]
        else:
            print('-1')
    elif command=='size':
        print(len(li_queue))
    elif command=='empty':
        if li_queue:
            print('0')
        else:
            print('1')
    elif command=='front':
        if li_queue:
            print(li_queue[0])
        else:
            print('-1')
    elif command=='back':
        if li_queue:
            print(li_queue[-1])
        else:
            print('-1')