N, M = map(int, input().split())

li_queue = list(range(1,N+1))
jimin_queue = input().split()
for i in range(len(jimin_queue)):
    jimin_queue[i] = int(jimin_queue[i])

cnt = 0
min_value = []

while(jimin_queue):
    if li_queue[0]==jimin_queue[0]:
        del li_queue[0]
        del jimin_queue[0]
    else:
        min_value.clear()
        for idx, j in enumerate(li_queue):
            if jimin_queue[0]==j:
                min_value.append(idx)
                break
        for idx, j in enumerate(li_queue[::-1]):
            if jimin_queue[0]==j:
                min_value.append(idx+1)
                break

        if min_value[0]<min_value[1]:
            for i in range(min_value[0]):
                li_queue.append(li_queue[0])
                del li_queue[0]
                cnt+=1
        else:
            for i in range(min_value[1]):
                li_queue.insert(0,li_queue[-1])
                del li_queue[-1]
                cnt+=1

print(cnt)