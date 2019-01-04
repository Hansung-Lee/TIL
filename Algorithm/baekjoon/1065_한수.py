N = input()

cnt = 99


if (len(N)==1):
    cnt = int(N)
elif (len(N)==2):
    cnt = int(N)
elif (len(N)==3):
    for i in range(100,int(N)+1):
        if(int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2])):
            cnt+=1
elif (N=='1000'):
    cnt = 144

print(cnt)