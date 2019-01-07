msg = input()

A = msg.split()[0]
B = msg.split()[1]

new_A = int(A[::-1])
new_B = int(B[::-1])

if(new_A<new_B):
    print(new_B)
else:
    print(new_A)