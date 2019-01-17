T = int(input())

for t in range(T):
    N = int(input())
    dict_clothes = {}
    for n in range(N):
        clothes = input().split()
        if clothes[1] in dict_clothes.keys():
            dict_clothes[clothes[1]] += 1
        else:
            dict_clothes[clothes[1]] = 1
    
    result = 1
    for cnt in dict_clothes.values():
        result *= (cnt+1)
    
    print(result-1)