N = int(input())
li = [0, 0, 1]

for i in range(2, (N//3)):
    li.append(li[-1]+i)
    
print(li[(N//3)-1])