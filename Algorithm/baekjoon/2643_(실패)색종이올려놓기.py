N = int(input())
paper = []

for n in range(N):
    paper.append(list(map(int, input().split())))

paper.sort()

dp = [1] * N

now_paper = paper[n]
result = 1

for i in range(1,len(paper)):
    if (now_paper[0] <= paper[i][0] and now_paper[1] <= paper[i][1]) or \
        (now_paper[0] <= paper[i][1] and now_paper[1] <= paper[i][0]):
        now_paper = paper[i]
        result += 1

print(max_value)