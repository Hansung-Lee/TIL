N = int(input())
li = [0, 3]

for n in range(2,N+1):
    li.append(li[-1]+(3*n*(n+1))//2)

print(li[N])