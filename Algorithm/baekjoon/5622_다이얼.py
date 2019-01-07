msg = input()

li = []

for m in msg:
    if (m=='A' or m=='B' or m=='C'):
        li.append(2)
    elif (m=='D' or m=='E' or m=='F'):
        li.append(3)
    elif (m=='G' or m=='H' or m=='I'):
        li.append(4)
    elif (m=='J' or m=='K' or m=='L'):
        li.append(5)
    elif (m=='M' or m=='N' or m=='O'):
        li.append(6)
    elif (m=='P' or m=='Q' or m=='R' or m=='S'):
        li.append(7)
    elif (m=='T' or m=='U' or m=='V'):
        li.append(8)
    elif (m=='W' or m=='X' or m=='Y' or m=='Z'):
        li.append(9)

sum1 = 0

for j in li:
    if(j==2):
        sum1+=3
    elif(j==3):
        sum1+=4
    elif(j==4):
        sum1+=5
    elif(j==5):
        sum1+=6
    elif(j==6):
        sum1+=7
    elif(j==7):
        sum1+=8
    elif(j==8):
        sum1+=9
    elif(j==9):
        sum1+=10
print(sum1)