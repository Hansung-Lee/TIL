msg = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
li = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

msg = msg.lower()


for i in msg:
    if (i =='a'):
        li[0] +=1
    elif (i =='b'):
        li[1] +=1
    elif (i =='c'):
        li[2] +=1
    elif (i =='d'):
        li[3] +=1
    elif (i =='e'):
        li[4] +=1
    elif (i =='f'):
        li[5] +=1
    elif (i =='g'):
        li[6] +=1
    elif (i =='h'):
        li[7] +=1
    elif (i =='i'):
        li[8] +=1
    elif (i =='j'):
        li[9] +=1
    elif (i =='k'):
        li[10] +=1
    elif (i =='l'):
        li[11] +=1
    elif (i =='m'):
        li[12] +=1
    elif (i =='n'):
        li[13] +=1
    elif (i =='o'):
        li[14] +=1
    elif (i =='p'):
        li[15] +=1
    elif (i =='q'):
        li[16] +=1
    elif (i =='r'):
        li[17] +=1
    elif (i =='s'):
        li[18] +=1
    elif (i =='t'):
        li[19] +=1
    elif (i =='u'):
        li[20] +=1
    elif (i =='v'):
        li[21] +=1
    elif (i =='w'):
        li[22] +=1
    elif (i =='x'):
        li[23] +=1
    elif (i =='y'):
        li[24] +=1
    elif (i =='z'):
        li[25] +=1


M=[]

m = max(li)

for i in li:
    if i==m:
        M.append(i)

if (len(M)==1):
    print(alphabet[li.index(max(li))].upper())
elif(len(msg)==0):
    print('')
else:
    print('?')