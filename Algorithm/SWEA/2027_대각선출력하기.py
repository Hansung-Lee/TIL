cnt =0
for i in range(5):
    for j in range(5):
        if(cnt==j): print("#",end='')
        else: print("+",end='')
    print('')    
    cnt+=1
