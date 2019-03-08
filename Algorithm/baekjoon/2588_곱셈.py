A = input()
B = input()

result = 0

for i in range(3):
    temp = 0
    for j in range(3):
        temp += int(B[2-i])*int(A[2-j])*(10**j)
    
    print(temp)
    result += temp*(10**i)

print(result)