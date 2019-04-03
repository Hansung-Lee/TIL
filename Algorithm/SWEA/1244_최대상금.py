import itertools


def change(nums):
    result = []
    for j in range(len(nums)):
        for i in range(len(li_comb)):
            temp = list(nums[j])
            temp[li_comb[i][0]], temp[li_comb[i][1]] = temp[li_comb[i][1]], temp[li_comb[i][0]]
            result.append(''.join(temp))

    result.sort()

    return [result[-2], result[-1]]


T = int(input())

for t in range(T):
    nums, cnt = map(str, input().split())
    li_comb = list(itertools.combinations(range(len(nums)), 2))

    nums = [nums]

    for i in range(int(cnt)):
        nums = change(nums)

    print("#{} {}".format(t+1, nums[-1]))