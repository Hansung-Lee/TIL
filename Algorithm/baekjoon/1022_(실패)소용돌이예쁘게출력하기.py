r1, c1, r2, c2 = map(int, input().split())

max_rc = max(abs(r1),abs(c1),abs(r2),abs(c2))
limit = max_rc*2 + 1
li = [[0 for y in range(limit)] for x in range(limit)]

direction = ['up', 'left', 'down', 'right']
cnt = 1
row = max_rc
column = max_rc
li[row][column] = 1
li[row][column+1] = 2
column+=1

def row_column(direction_, row_, column_):
    if direction_ == direction[0]:
        row_-=1
    elif direction_ == direction[1]:
        column_-=1
    elif direction_ == direction[2]:
        row_+=1
    elif direction_ == direction[3]:
        column_+=1
    
    return row_, column_

num = 3

for i in range(max_rc):
    for z in range(4):
        for j in range(cnt):
            row, column = row_column(direction[z], row, column)
            li[row][column] = num
            num+=1
        if z==0 or z==2:
            cnt+=1
            if z==2 and i==max_rc-1:
                cnt-=1
    
for i in range(abs(r1-r2)+1):
    li_print = []
    for j in range(abs(c1-c2)+1):
        li_print.append(str(li[r1+max_rc+i][c1+max_rc+j]))
    print(' '.join(li_print))