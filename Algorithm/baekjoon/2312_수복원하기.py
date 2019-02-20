T = int(input())

for t in range(T):
    N = int(input())
    li = [0] * (N-1)

    for i in range(len(li)):
        while not N%(i+2):
            N = N//(i+2)
            li[i] += 1
    
    for i in range(len(li)):
        if li[i]:
            print (f"{i+2} {li[i]}")