N = int(input())

for i in range(N):
    result = i
    for stri in str(i):
        result += int(stri)
    
    if result == N:
        print(i)
        break
    elif i == N-1:
        print(0)
        break