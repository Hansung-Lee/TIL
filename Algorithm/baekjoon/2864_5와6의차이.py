A, B = input().split()

min_value = 0
max_value = 0

for i in range(len(A)):
    if A[i] == '5' or A[i] == '6':
        min_value += 5*(10**(len(A)-1-i))
        max_value += 6*(10**(len(A)-1-i))
    else:
        min_value += int(A[i])*(10**(len(A)-1-i))
        max_value += int(A[i])*(10**(len(A)-1-i))

for i in range(len(B)):
    if B[i] == '5' or B[i] == '6':
        min_value += 5*(10**(len(B)-1-i))
        max_value += 6*(10**(len(B)-1-i))
    else:
        min_value += int(B[i])*(10**(len(B)-1-i))
        max_value += int(B[i])*(10**(len(B)-1-i))

print(min_value, max_value)