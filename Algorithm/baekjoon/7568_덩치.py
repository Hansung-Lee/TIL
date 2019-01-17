N = int(input())
li_people = []
li_score = []

for i in range(N):
    li_people.append(input().split())

for me in li_people:
    k = 1
    for you in li_people:
        if me[0] < you[0] and me[1] < you[1]:
            k += 1
    li_score.append(str(k))

print(' '.join(li_score))