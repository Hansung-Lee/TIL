T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))

    result = 0

    for i in range(len(li)):
        result += li[i]//K

    print(result)