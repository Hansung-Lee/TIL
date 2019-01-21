M = int(input())
N = int(input())

li = [i**2 for i in range(1,101)]

result = 0
max_value = 0

for j in range(N,M-1,-1):
    if j in li:
        result += j
        max_value = j

if result:
    print(result)
    print(max_value)
else:
    print(-1)