T = int(input())

for t in range(T):
    N = int(input())
    li = [1,1,1,2,2,3]
    
    for n in range(N-6):
        li.append(li[-2]+li[-3])

    print(li[N-1])