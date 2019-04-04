import itertools
import copy

def down_stair(li, stair_num):
    queue = []

    for i in range(len(li)):
        distance = abs(people[li[i]][0] - stairs[stair_num][0]) + abs(people[li[i]][1] - stairs[stair_num][1])
        queue.append([distance, stairs[stair_num][2]])
    
    queue.sort()
    result = 0
    if queue:
        result = queue[0][0]

    while queue:
        result += 1

        for i in range(min(3,len(queue))):
            if result > queue[i][0]:
                queue[i][1] -= 1

        temp_queue = []
        for i in range(len(queue)):
            if queue[i][1]:
                temp_queue.append(queue[i][:])
        queue = copy.deepcopy(temp_queue)

    return result+1


def check(comb):
    global min_value

    temp = [x for x in range(len(people))]
    for c in comb:
        temp.remove(c)
    
    val = max(down_stair(comb, 0), down_stair(temp, 1))

    if min_value > val:
        min_value = val


T = int(input())

for t in range(T):
    N = int(input())
    li = []
    people = []
    stairs = []

    for n in range(N):
        li.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if li[i][j]:
                if li[i][j] == 1:
                    people.append([i, j])
                else:
                    stairs.append([i, j, li[i][j]])

    li_combs = [()]
    for i in range(len(people)):
        li_combs.extend(list(itertools.combinations(range(len(people)), i+1)))

    min_value = 9999

    for i in range(len(li_combs)):
        check(list(li_combs[i]))

    print("#{} {}".format(t+1, min_value))