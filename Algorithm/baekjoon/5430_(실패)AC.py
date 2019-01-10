import sys

T = int(sys.stdin.readline())

for t in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    li = sys.stdin.readline().strip()[1:-1].split(',')
    if not li[0]:
        li.clear()
    error = False
    answer = ''

    for i in p:
        if not li:
            error=True
            break
        else:
            if i=='R':
                li = li[::-1]
            elif i=='D':
                try:
                    del li[0]
                except:
                    error=True
                    break
    if error:
        print('error')
    else:
        answer = str(li).replace(" ", "")
        answer = answer.replace("'", "")
        print(answer)