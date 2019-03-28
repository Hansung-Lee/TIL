T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    
    li = []
    for n in range(N):
        li.append(int(input()))

    gates = li[:]
    humans = 0
    times = 0

    while humans != M:
        temp_min = min(gates)
        times += temp_min

        for i in range(len(gates)):
            gates[i] -= temp_min

            if gates[i] == 0:
                gates[i] = li[i]
                humans += 1
                if humans == M:
                    break

    print("#{} {}".format(t+1, times))