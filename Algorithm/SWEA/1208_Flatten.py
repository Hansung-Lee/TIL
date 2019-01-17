def find_max_min(li_box):
    max_box = 0
    max_box_idx = 0
    min_box = 101
    min_box_idx = 0

    for i in range(len(li_box)):
        if li_box[i] > max_box:
            max_box = li_box[i]
            max_box_idx = i
        if li_box[i] < min_box:
            min_box = li_box[i]
            min_box_idx = i
    return max_box, max_box_idx, min_box, min_box_idx

for t in range(10):
    D = int(input())
    li_box = list(map(int, input().split()))

    for dump in range(D):
        max_box, max_box_idx, min_box, min_box_idx = find_max_min(li_box)
        li_box[max_box_idx] -= 1
        li_box[min_box_idx] += 1
    
    max_box, max_box_idx, min_box, min_box_idx = find_max_min(li_box)

    print(f"#{t+1} {max_box-min_box}")