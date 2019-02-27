def make_clock(num):
    result = 10000

    for i in range(4):
        temp = int(num[(i%4)])*1000 + int(num[((i+1)%4)])*100 + int(num[((i+2)%4)])*10 + int(num[((i+3)%4)])
        if result > temp:
            result = temp

    return result

li_N = input().split()

clock_num = 10000

for i in range(4):
    num = int(li_N[(i%4)])*1000 + int(li_N[((i+1)%4)])*100 + int(li_N[((i+2)%4)])*10 + int(li_N[((i+3)%4)])
    if clock_num > num:
        clock_num = num

li_clocks = []

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                li_clocks.append(make_clock(str(a) + str(b) + str(c) + str(d)))

li_clocks = list(set(li_clocks))
li_clocks.sort()

i = 0
while True:
    if li_clocks[i] == clock_num:
        break
    i += 1

print(i+1)