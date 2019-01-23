K = 1000 - int(input())
li_N = [500, 100, 50, 10, 5, 1]

result = 0

while K!=0:
    for n in li_N:
        if K>=n:
            K=K-n
            result +=1
            break
        else:
            del li_N[0]
            break

print(result)