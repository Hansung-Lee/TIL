import sys

T = int(sys.stdin.readline())

for i in range(T):
    temp = sys.stdin.readline()
    R = int(temp.split()[0])
    S = temp.split()[1]

    li_print=[]

    for s in S:
        for r in range(R):
            li_print.append(s)

    for z in li_print:
        print(z, end="")
    print('')