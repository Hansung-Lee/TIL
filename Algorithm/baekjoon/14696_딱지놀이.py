N = int(input())

for n in range(N):
    A = [0,0,0,0,0] # 세모(1), 네모(2), 동그라미(3), 별(4)
    B = [0,0,0,0,0]

    li = list(map(int, input().split()))
    for i in range(1, len(li)):
        A[li[i]] += 1
    li = list(map(int, input().split()))
    for i in range(1, len(li)):
        B[li[i]] += 1
    
    for i in range(4, 0, -1):
        if A[i] > B[i]:
            print('A')
            break
        elif A[i] < B[i]:
            print('B')
            break
        else:
            if i == 1:
                print('D')