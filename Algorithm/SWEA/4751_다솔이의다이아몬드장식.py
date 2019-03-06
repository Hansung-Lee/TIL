T = int(input())

for t in range(T):
    li = ['..#..', '.#.#.', '#.{}.#', '.#.#.', '..#..']
    result = ['.', '.', '.', '.', '.']
    word = input().strip()
    if len(word) == 1:
        for i in range(len(li)):
            if i == 2:
                print(li[i].format(word))
            else:
                print(li[i])
    else:
        for i in range(len(word)):
            for j in range(len(li)):
                if j == 2:
                    result[j] = result[j][:-1]
                    result[j] += li[j].format(word[i])
                else:
                    result[j] = result[j][:-1]
                    result[j] += li[j]

        for i in range(len(result)):
            print(result[i])