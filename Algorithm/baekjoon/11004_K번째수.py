N, K = map(int, input().split())
li_A = list(map(int, input().split()))

li_A.sort()
print(li_A[K-1])