def partial(pattern):
    ret = [0]
    
    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret
    
def kmp(T, P):
    part, ret, j = partial(P), [], 0

    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = part[j - 1]
        if T[i] == P[j]: j += 1
        if j == len(P):
            ret.append(i - (j - 1))
            j = 0
    return len(ret)


H = input()
N = input()

print(kmp(H, N))