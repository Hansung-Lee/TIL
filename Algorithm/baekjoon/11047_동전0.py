N, K = map(int, input().split())
li_N = []
for n in range(N):
    li_N.append(int(input()))

li_N = li_N[::-1]

result = 0

while K!=0:
    for n in li_N:
        if K>=n:
            K=K-n
            result +=1
            break
        else:
            del li_N[0]
            break

print(result)