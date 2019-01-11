result = {
    0:'D', # 윷
    1:'C', # 걸
    2:'B', # 개
    3:'A', # 도
    4:'E'  # 모
}
for i in range(3):
    n = sum(map(int,input().split()))
    print(result[n])