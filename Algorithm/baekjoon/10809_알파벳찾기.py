S = input()
li = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

new_S = S[::-1]

index = len(new_S)-1

for i in new_S:
    if (i =='a'):
        li[0] = index
    elif (i =='b'):
        li[1] = index
    elif (i =='c'):
        li[2] = index
    elif (i =='d'):
        li[3] = index
    elif (i =='e'):
        li[4] = index
    elif (i =='f'):
        li[5] = index
    elif (i =='g'):
        li[6] = index
    elif (i =='h'):
        li[7] = index
    elif (i =='i'):
        li[8] = index
    elif (i =='j'):
        li[9] = index
    elif (i =='k'):
        li[10] = index
    elif (i =='l'):
        li[11] = index
    elif (i =='m'):
        li[12] = index
    elif (i =='n'):
        li[13] = index
    elif (i =='o'):
        li[14] = index
    elif (i =='p'):
        li[15] = index
    elif (i =='q'):
        li[16] = index
    elif (i =='r'):
        li[17] = index
    elif (i =='s'):
        li[18] = index
    elif (i =='t'):
        li[19] = index
    elif (i =='u'):
        li[20] = index
    elif (i =='v'):
        li[21] = index
    elif (i =='w'):
        li[22] = index
    elif (i =='x'):
        li[23] = index
    elif (i =='y'):
        li[24] = index
    elif (i =='z'):
        li[25] = index
    index-=1

for z in li:
    print(z, end=" ")