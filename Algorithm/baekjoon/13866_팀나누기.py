li = list(map(int, input().split()))

min_value = 99999

for i in range(1, 4):
    level = li[0] + li[i]
    if abs(sum(li)-(2*level)) < min_value:
        min_value = abs(sum(li)-(2*level))

print(min_value)