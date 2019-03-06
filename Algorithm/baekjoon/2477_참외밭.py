K = int(input())

li = []

max_garo = 0
max_sero = 0

for i in range(6):
    a, b = map(int, input().split())
    li.append((a, b))

for i in li:
    a, b = i
    if a == 1:
        if max_garo < b:
            max_garo = b
    elif a == 2:
        if max_garo < b:
            max_garo = b
    elif a == 3:
        if max_sero < b:
            max_sero = b
    else:
        if max_sero < b:
            max_sero = b

small_garo = 0
small_sero = 0

for i in range(len(li)):
    a, b = li[i]
    if a == 1 or a == 2:
        if b == max_garo:
            small_sero = min(li[i-1][1], li[(i+1)%6][1])
    
    if a == 3 or a == 4:
        if b == max_sero:
            small_garo = min(li[i-1][1], li[(i+1)%6][1])

area = max_garo*max_sero - ((max_garo-small_garo)*(max_sero-small_sero))

print(K*area)