li = []
new_li = []

for i in range(5):
    li.append(int(input()))

for j in li:
    if (j<40):
        new_li.append(40)
    else:
        new_li.append(j)

sum_li = sum(new_li)
avg_li = int(sum_li/5)

print(avg_li)