N = int(input())
li = []
result = []

for n in range(N):
    li.append(int(input()))

if len(li)==1:
    print(li[0])
elif len(li)<4:
    print(sum(li[0]+li[-1]))

else:
    for i in range():
        if i==0:
            result.append([li[i], li[i+1]])
        else:
            result.append(li[i])