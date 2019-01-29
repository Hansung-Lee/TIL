N = int(input())
li = [2**i for i in range(1,20)]

if N==1:
    print(1)
else:
    for idx, num in enumerate(li):
        if num == N:
            print(num)
            break
        elif num > N:
            print((N-(2**(idx)))*2)
            break