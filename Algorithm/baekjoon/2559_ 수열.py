N, K = map(int, input().split())
li = list(map(int, input().split()))

max_value = sum(li[:K])
temp = max_value

for i in range(len(li)-K):
    temp = temp - li[i] + li[i+K]
    if max_value < temp:
        max_value = temp

print(max_value)