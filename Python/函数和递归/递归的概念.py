#循环定义
#递归
#
def Factorial(n):
    if n < 2:
        return 1
    else:
        return n * Factorial(n-1)
print(Factorial(24))
def Fib(n):
    if n < 3:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(10))
def f(n,m):
    if n == 0:
        return m
    elif m == 0:
        return n
    else:
        if n >= m:
            return f(m,n-m) + 1
        else:
            return f(n,m-n) + 2
print(f(3,4))