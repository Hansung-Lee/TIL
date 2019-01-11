n = int(input())
num_fib_a = 1
num_fib_b = 1
if n>1:
    for i in range(n-1):
        num_fib_a, num_fib_b = num_fib_b, num_fib_a+num_fib_b
elif n==0:
    num_fib_a = 0
print (num_fib_a)