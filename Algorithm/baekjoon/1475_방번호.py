N = input()

li = [1,1,1,1,1,1,0,1,1,2]

cnt = 1

for n in N:
    if (n=='6' or n=='9'):
        if(li[9]>0):
            li[9]-=1
        else:
            for i in range(10):
                li[i]+=1
            li[9]=1
            cnt+=1
    else:
        if(li[int(n)]>0):
            li[int(n)]-=1
        else:
            for i in range(10):
                li[i]+=1
            li[int(n)] = 0
            cnt+=1
print(cnt)