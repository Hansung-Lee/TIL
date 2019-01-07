N = int(input())

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
li = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

seq = 0
cnt = 0
tf = True

for i in range(N):
    msg = input()
    seq = 0
    tf = True
    li = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    for i in msg:
        for j in alphabet:
            if (i == j):
                if(li[alphabet.index(j)]==-1):
                    li[alphabet.index(j)] +=1
                    seq=alphabet.index(j)+1
                elif(seq==alphabet.index(j)+1):
                    li[alphabet.index(j)] +=1
                else:
                    tf=False
    if(tf):
        cnt+=1
print(cnt)