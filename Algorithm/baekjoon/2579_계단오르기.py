N = int(input())
li = []
result = []

for n in range(N):
    li.append(int(input()))

for i in range(len(li)):
    if i==0:
        result.append(li[i])
    elif i==1:
        result.append(li[i]+li[0])
    elif i==2:
        result.append(li[i]+max(li[0],li[1]))
    else:
        result.append(li[i]+max(result[i-2],li[i-1]+result[i-3]))

print(result[-1])