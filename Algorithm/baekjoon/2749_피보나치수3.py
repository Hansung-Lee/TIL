mod = 1000000
p = mod//10*15
list = [0,1]

n = int(input())

for i in range(2,p):
    list.append(list[i-1]+list[i-2])
    list[i] = list[i]%mod

print(list[n%p])