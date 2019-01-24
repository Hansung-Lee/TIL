N = int(input())

li = [0,1,2,3]

for n in range(N-3):
    li.append(li[-1] + li[-2])

print(li[N]%10007)