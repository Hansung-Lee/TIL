msg = input()

cnt = len(msg)
check = 0

for m in msg:
    if(m=='c'):
        check = 1
    elif(m=='d'):
        check = 2
    elif(m=='z' and check!=2):
        check = 3
    elif(m=='l'):
        check = 4
    elif(m=='n'):
        check = 5
    elif(m=='s'):
        check = 6

    elif(check == 1):
        if(m=='=' or m=='-'):
            cnt-=1
            check = 0
    elif(check == 2):
        if(m=='-'):
            cnt-=1
            check = 0
        elif(m=='z'):
            check = 21
    elif(check==21):
        if(m=='='):
            cnt-=2
            check = 0
    elif(check==3):
        if(m=='='):
            cnt-=1
            check = 0
    elif(check==4):
        if(m=='j'):
            cnt-=1
            check = 0
    elif(check==5):
        if(m=='j'):
            cnt-=1
            check = 0
    elif(check==6):
        if(m=='='):
            cnt-=1
            check = 0
print(cnt)