#lambda表达式 一次性函数
#稳定的排序
a = [100, -10, -11, 111]
a.sort(key = lambda x: str(x)[0])
print(a)
k = lambda x,y : x+y
print(k(4,5))
print(ord('1'))

#多级排序
def f(x):
    x = str(x)
    return (x[0],x[1],x[2])
a.sort(key=f)
print(a)

#元组不可修改, 故没有sort, 只能sorted
a = 12,3,4
b = sorted(a)
print(b)