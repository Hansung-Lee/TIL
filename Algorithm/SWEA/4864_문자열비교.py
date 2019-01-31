def bruteForce(p, t):
    N = len(t)
    M = len(p)
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M: return 1
    else: return 0

T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()
    print(f"#{t+1} {bruteForce(str1,str2)}")