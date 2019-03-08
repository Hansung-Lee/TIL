T = int(input())

for t in range(T):
    N = int(input())
    result = ''

    for n in range(N):
        input_ = input().split()
        result += input_[0]*int(input_[1])

    print("#{}".format(t+1))

    for i in range(((len(result)-1)//10)+1):
        print(result[10*i:(10*i)+10])