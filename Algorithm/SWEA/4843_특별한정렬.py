T = int(input())
for t in range(T):
    N = int(input())
    li_N = list(map(int, input().split()))

    for i in range(len(li_N) - 1):
        min = i
        for j in range(i + 1, len(li_N)):
            if li_N[min] > li_N[j]:
                min = j
        li_N[i], li_N[min] = li_N[min], li_N[i]

    temp_a = []
    temp_b = []

    for n in li_N[:N//2]:
        temp_a.append(n)
    for n in li_N[N//2:][::-1]:
        temp_b.append(n)

    result = []

    for num in range(N//2):
        result.append(temp_b[num])
        result.append(temp_a[num])

    if N%2==1:
        result.append(temp_b[-1])

    str_ = ''
    limit = 10
    if len(result)<limit:
        limit = len(result)

    for i in range(limit):
        str_ += str(result[i])+' '

    print(f"#{t+1} {str_}")