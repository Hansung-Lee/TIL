import sys

N = int(sys.stdin.readline().rstrip())

result = 1
for n in range(N):
    M = int(sys.stdin.readline().rstrip())
    result += (M-1)
    
print(result)