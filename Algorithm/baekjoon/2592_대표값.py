li = []

for i in range(10):
    li.append(int(input()))

print(sum(li)//10)

li_cnt = [0]*(max(li)+1)

for i in range(len(li)):
    li_cnt[li[i]] += 1

print(li_cnt.index(max(li_cnt)))