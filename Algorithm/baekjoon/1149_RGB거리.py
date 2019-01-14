import sys

N = int(sys.stdin.readline())
li = []
result = []

for n in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(li)):
    if i>1:
        result.append([min(result[i-1][1],result[i-1][2])+li[i][0],
                    min(result[i-1][0],result[i-1][2])+li[i][1],
                    min(result[i-1][0],result[i-1][1])+li[i][2]])
    elif i==0:
        result.append([li[i][0], li[i][1], li[i][2]])
        
print(min(result[-1]))