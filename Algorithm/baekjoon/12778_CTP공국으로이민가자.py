T = int(input())

for t in range(T):
    n, type_ = map(str, input().split())
    question = input().split()

    result = ""

    if type_ == 'C':
        for q in question:
            result += f"{ord(q)-64} "
    else:
        for q in question:
            result += f"{chr(int(q)+64)} "
    print(result)