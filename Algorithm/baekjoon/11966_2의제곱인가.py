N = int(input())

result = 0

if N == 1:
    result = 1

for i in range(31):
    if N == (2<<i):
        result = 1
        break

print(result)