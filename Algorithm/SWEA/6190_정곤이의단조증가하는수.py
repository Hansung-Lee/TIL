def check_danjo(num):
    num = str(num)
    if num[0] == num[-1]:
        return False
    for n in range(len(str(num))-1):
        if int(num[n]) > int(num[n+1]):
            return False
    return True


T = int(input())

for t in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    max_value = -1

    for i in range(len(li)):
        for j in range(len(li)):
            if i < j:
                num = li[i] * li[j]
                if check_danjo(num):
                    if max_value < num:
                        max_value = num

    print("#{} {}".format(t+1, max_value))