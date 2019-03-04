N = int(input())
result = []
max_value = 0
max_mon = ''

for n in range(N):
    mon = input()
    K, M = map(int, input().split())

    cnt = 0

    while M >= K:
        M -= K
        M += 2
        cnt += 1
    
    result.append(cnt)

    if max_value < cnt:
        max_value = cnt
        max_mon = mon

print(sum(result))
print(max_mon)