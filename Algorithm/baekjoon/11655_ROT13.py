msg = input()

result = ""

for m in msg:
    code = ord(m)
    if 64 < code < 91:
        code += 13
        if code > 90:
            code -= 26
        result += chr(code)
    elif 96 < code < 123:
        code += 13
        if code > 122:
            code -= 26
        result += chr(code)
    else:
        result += m

print(result)