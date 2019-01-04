import sys

a, b, c = map(int, sys.stdin.readline().split())

if (a>b):
    if (c>a):
        print(a)
    elif (b>c):
        print(b)
    elif (a>c):
        if (b>c):
            print(b)
        elif (c>b):
            print(c)
    elif (c>b):
        if (a>c):
            print(c)
        elif (c>a):
            print(a)
elif (b>a):
    if (c>b):
        print(b)
    elif (a>c):
        print(a)
    elif (b>c):
        if (a>c):
            print(a)
        elif (c>a):
            print(c)
    elif (c>a):
        if (b>c):
            print(c)
        elif (c>b):
            print(b)