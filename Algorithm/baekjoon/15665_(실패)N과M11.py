def func(m):
    global result
    global li_print
    if m == 0:
        li_print.append(' '.join([str(x) for x in result]))
    else:
        for i in range(len(li)):
            result.append(li[i])
            func(m-1)
            result.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

result = []
li_print = []
func(M)
li_print = list(set(li_print))
li_print.sort()

for p in li_print:
    print(p)