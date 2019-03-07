def func(m):
    global result
    if m == 0:
        print(' '.join([str(x) for x in result]))
    else:
        for i in range(len(li)):
            if not result:
                result.append(li[i])
                func(m-1)
                result.pop()
            elif li[i]>= result[-1]:
                result.append(li[i])
                func(m-1)
                result.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

result = []
func(M)