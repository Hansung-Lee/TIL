def merge_sort(li):
    global cnt
    if len(li) == 1:
        return li
    
    if len(li) == 2:
        if li[0] <= li[1]:
            return li
        else:
            cnt += 1
            return [li[1], li[0]]

    mid = len(li)//2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])

    li_return = [0] * len(li)

    idx = 0
    lidx = 0
    ridx = 0

    while lidx < len(left) or ridx < len(right):
        if lidx < len(left) and ridx < len(right):
            if left[lidx] <= right[ridx]:
                li_return[idx] = left[lidx]
                lidx += 1
            else:
                li_return[idx] = right[ridx]
                ridx += 1
        elif lidx < len(left):
            if lidx == len(left)-1:
                cnt += 1
            li_return[idx] = left[lidx]
            lidx += 1
        elif ridx < len(right):
            li_return[idx] = right[ridx]
            ridx += 1
        idx += 1

    return li_return


T = int(input())

for t in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    cnt = 0
    result = merge_sort(li)
    print("#{} {} {}".format(t+1, result[N//2], cnt))
