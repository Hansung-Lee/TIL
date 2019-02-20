bracket = input()

stack = []
result = 0
open_tf = True

for b in bracket:
    if b =='(':
        open_tf = True
        stack.append(b)
    else:
        stack.pop()
        if open_tf:
            result += len(stack)
            open_tf = False
        else:
            result += 1
print(result)