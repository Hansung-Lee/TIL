T = int(input())

for t in range(T):
    li = []
    for i in range(5):
        li.append(list(input()))

    max_len = max([len(l) for l in li])

    for i in range(len(li)):
        for j in range(max_len-len(li[i])):
            li[i].append(' ')

    result = ''
    for j in range(len(li[0])):
        for i in range(len(li)):
            result += li[i][j]

    answer = ""
    for r in result:
        if not r == " ":
            answer += r

    print("#{} {}".format(t+1,answer))