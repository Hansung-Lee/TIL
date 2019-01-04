vals = []

def d(n):
    sum = n
    for i in str(n):
        sum = sum + int(i)

    vals.append(sum)

for num in range(10000):
    d(num)

for i in range(10000):
    if i in vals:
        pass
    else:
        print(i)