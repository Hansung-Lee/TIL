def check(idx):
    sum_ = 0

    for i in range(idx, -1, -1):
        sum_ += triangle_num[i]
        if sum_ < N:
            for j in range(i, -1, -1):
                sum_ += triangle_num[j]
                if sum_ < N:
                    for q in range(j, -1, -1):
                        sum_ += triangle_num[q]
                        if sum_ == N:
                            return True
                        sum_ -= triangle_num[q]
                sum_ -= triangle_num[j]
        sum_ -= triangle_num[i]
    return False


triangle_num = []
sum_ = 0

for i in range(1, 46):
    sum_ += i
    triangle_num.append(sum_)

T = int(input())

for t in range(T):
    N = int(input())
    idx = 0
    for i in range(len(triangle_num)):
        if N <= triangle_num[i]:
            idx = i - 1
            break

    if check(idx):
        print(1)
    else:
        print(0)