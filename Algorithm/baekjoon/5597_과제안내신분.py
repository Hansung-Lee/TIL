li = [False] * 31
li[0] = True

for i in range(28):
    li[int(input())] = True

for i in range(len(li)):
    if not li[i]:
        print(i)