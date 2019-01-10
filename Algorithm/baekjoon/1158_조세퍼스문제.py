N, M = map(int, input().split())

li_N = [i for i in range(1,N+1)]
li_answer = []
idx = 0

for i in range(N):
    for j in range(M-1):
        idx+=1
        if idx==len(li_N):
            idx=0
    li_answer.append(li_N[idx])
    del li_N[idx]

    if idx >= len(li_N):
        idx = 0

result = '<' + str(li_answer)[1:-1] + '>'

print(result)