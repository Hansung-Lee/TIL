N = input()

if int(N)<10:
    N = '0' + N

N1=''
cnt=0

while(N!=N1):
    if (cnt==0):
        a = str(int(N[0]) + int(N[1]))
        if int(a)<10:
            a = '0' + a
        b = N[1] + a[1]
        N1 = b
        cnt+=1
    else:
        a = str(int(N1[0]) + int(N1[1]))
        if int(a)<10:
            a = '0' + a
        b = N1[1] + a[1]
        N1 = b
        cnt+=1

print(cnt)