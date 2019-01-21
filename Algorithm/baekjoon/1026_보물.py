N = int(input())
li_A = list(map(int, input().split()))
li_B = list(map(int, input().split()))

li_A = sorted(li_A)[::-1]
li_B.sort()

S = 0
for n in range(N):
    S += li_A[n]*li_B[n]

print(S)