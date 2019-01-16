import sys
N = int(sys.stdin.readline())

li = []
li_count = []
new_li = [0] * N

max_num = 0

for n in range(N):
    num = int(sys.stdin.readline())
    li.append(num)
    if num > max_num:
        max_num = num

li_count = [0] * max_num

for l in li:
    li_count[l-1] += 1

for i in range(1,len(li_count)):
    li_count[i] += li_count[i-1]

for l in li[::-1]:
    new_li[li_count[l-1]-1] = l
    li_count[l-1] -= 1

for p in new_li:
    print(p)