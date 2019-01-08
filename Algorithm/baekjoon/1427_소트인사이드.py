N = input()

li = []

for n in N:
    li.append(int(n))

li.sort(reverse=True)


print(''.join(str(e) for e in li))