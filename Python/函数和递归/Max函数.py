#函数可以没有返回值, 也可以返回多个值(元组)
def Max(x,y):
    if x > y:
        return x
    else:
        return y
n = Max(4,6)
print(n,Max(20,n))
print(Max("about","take"))