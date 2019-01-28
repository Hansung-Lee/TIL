K = int(input())
result = []

for k in range(K):
    n = int(input())

    if n == 0:
        del result[-1]
    else:
        result.append(n)

print(sum(result))