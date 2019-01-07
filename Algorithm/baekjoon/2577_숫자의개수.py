li_cnt = [0,0,0,0,0,0,0,0,0,0]

A = int(input())
B = int(input())
C = int(input())

mul = A*B*C

for x in str(mul):
    if x=='0':
        li_cnt[0]+=1
    elif x=='1':
        li_cnt[1]+=1
    elif x=='2':
        li_cnt[2]+=1
    elif x=='3':
        li_cnt[3]+=1
    elif x=='4':
        li_cnt[4]+=1
    elif x=='5':
        li_cnt[5]+=1
    elif x=='6':
        li_cnt[6]+=1
    elif x=='7':
        li_cnt[7]+=1
    elif x=='8':
        li_cnt[8]+=1
    elif x=='9':
        li_cnt[9]+=1

for i in li_cnt:
    print(i)