N = int(input())

result = [0,0,1,1]

for n in range(4,N+1):
    if not n%3:
        a = result[int(n/3)]
    else:
        a = 1000000
    if not n%2:
        b = result[int(n/2)]
    else:
        b = 1000000
    c = result[n-1]
    result.append(min(a,b,c)+1)

print(result[N])