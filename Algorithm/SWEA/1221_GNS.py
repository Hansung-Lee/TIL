T = int(input())

li_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for t in range(T):
    nono = input()
    msg = input().split()
    
    li_cnt = [0]*10

    for m in msg:
        for i in range(len(li_num)):
            if m == li_num[i]:
                li_cnt[i] += 1
    
    result = ''

    for i in range(len(li_cnt)):
        for j in range(li_cnt[i]):
            result += li_num[i] + ' '

    print(f"#{t+1} {result}")