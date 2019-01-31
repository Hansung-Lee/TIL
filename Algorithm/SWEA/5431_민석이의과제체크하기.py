T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    li_K = list(map(int, input().split())) 

    li_student = [i for i in range(1,N+1)]

    result = []

    for i in range(len(li_student)):
        submit_tf = True
        for j in range(len(li_K)):
            if li_student[i] == li_K[j]:
                submit_tf = False
                break
        if submit_tf:
            result.append(li_student[i])

    answer = ''

    for rst in result:
        answer += str(rst) + ' '

    print(f"#{t+1} {answer}")   