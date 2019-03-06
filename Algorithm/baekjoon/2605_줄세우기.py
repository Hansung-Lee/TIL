N = int(input())
input_ = list(map(int, input().split()))

li = []

for i in range(len(input_)):
    li.insert(input_[i], i+1)

li.reverse()

print(' '.join([str(x) for x in li]))