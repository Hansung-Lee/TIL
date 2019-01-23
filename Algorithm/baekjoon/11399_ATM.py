N = int(input())
li_P = list(map(int, input().split()))

li_P.sort()

temp_result = 0
result = 0

for p in li_P:
    temp_result = temp_result + p
    result += temp_result

print(result)