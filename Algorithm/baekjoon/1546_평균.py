import sys

N = int(sys.stdin.readline())

X = list(map(int, sys.stdin.readline().split()))

M = max(X)

new_X = []

for score in X:
    new_X.append(score/M*100)

print(sum(new_X)/len(new_X))