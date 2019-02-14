N = int(input())

result = []

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        result.append(f"{fromPole} {toPole}")
        moveTower(height-1,withPole,toPole,fromPole)

moveTower(N,"1","3","2")
print(len(result))
for r in result:
    print(r)