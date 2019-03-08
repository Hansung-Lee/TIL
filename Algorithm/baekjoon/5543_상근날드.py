sang = int(input())
jung = int(input())
ha = int(input())
coke = int(input())
cider = int(input())

burger = [sang, jung, ha]
drinks = [coke, cider]

min_value = 4000

for i in range(3):
    for j in range(2):
        num = burger[i] + drinks[j] - 50
        if min_value > num:
            min_value = num

print(min_value)