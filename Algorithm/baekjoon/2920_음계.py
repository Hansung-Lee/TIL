li=map(int,input().split())

check_asc = 1
check_des = 8

for i in li:
    if (i==check_asc):
        check_asc+=1
        check_des = 100
        if(check_asc==9):
            print('ascending')
    elif (i==check_des):
        check_asc = 100
        check_des-=1
        if(check_des==0):
            print('descending')
    else:
        print('mixed')
        break