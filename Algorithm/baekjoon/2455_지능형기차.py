li_people = []
people = 0

for i in range(4):
    a, b = map(int, input().split())
    people = people - a + b
    if people>10000:
        people = 10000
    li_people.append(people)

max_people = 0

for l in li_people:
    if l > max_people:
        max_people = l
print(max_people)