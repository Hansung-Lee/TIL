X = input()
N = len(X)
R = N%10

cnt = 0

for i in range(N//10):
    print(''.join(list(X)[cnt:cnt+10]))
    cnt+=10

if (R!= 0):
    print(''.join(list(X)[cnt:cnt+R]))