import itertools


def take_honey(points):
    li_combs = []
    for n in range(len(points)):
        li_combs.extend(list(itertools.combinations(points, n+1)))

    result = 0

    for n in range(len(li_combs)):
        temp = 0
        temp_c = 0
        comb = list(li_combs[n])
        for m in range(len(comb)):
            p = comb[m]
            temp += (li[p[0]][p[1]])**2
            temp_c += (li[p[0]][p[1]])
        if temp_c <= C and result < temp:
            result = temp
            
                
    return result


T = int(input())

for t in range(T):
    N, M, C = map(int, input().split())
    li = []
    for n in range(N):
        li.append(list(map(int, input().split())))

    max_value = 0

    for i in range(N):
        for j in range(N-M+1):
            li_a = []
            for q in range(M):
                li_a.append([i, j+q])
            result = take_honey(li_a)

            for i1 in range(i, N):
                for j1 in range(N-M+1):
                    li_b = []
                    breaker = False
                    for q in range(M):
                        li_b.append([i1, j1+q])
                        if [i1, j1+q] in li_a:
                            breaker = True
                            break
                    if breaker:
                        break
                    temp = take_honey(li_b)

                    if max_value < result + temp:
                        max_value = result + temp

    print("#{} {}".format(t+1, max_value))
