li = []
li2 = []
breaker = False

for i in range(9):
    li.append(int(input()))

for j in range(9):
    for z in range(j+1,9):
        li2 = li[:]
        del li2[z]
        del li2[j]
        if(sum(li2)==100):
            breaker = True
            break
    if breaker:
        break

li2.sort()
for p in li2:
    print(p)