import sys

C = int(sys.stdin.readline())

X = []
for n in range(C):
    X = list(map(int, sys.stdin.readline().split()))
    N = X[0]
    new_X = []

    for i in range(len(X)-1):
        new_X.append(X[i+1])

    avg = sum(new_X)/len(new_X)
    cnt = 0

    for x in new_X:
        if avg<x:
            cnt+=1
    
    score = cnt/len(new_X)*100

    print(str(format(round(score, 3),'.3f')) + "%")