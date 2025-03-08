# python中所有类都有__eq__方法
# x==y 为 x.__eq__(y)
# x没定义, y.__eq__(x)
# x,y 均没定义, x,y是整数常量不适用
# not a.__eq__(b) == a.__ne__(b)
print(24.5.__eq__(25))
a, b = 1, 13
print(a<b,a.__lt__(b))
print(a>b,a.__gt__(b))
print(a<=b,a.__le__(b))
print(a>=b,a.__ge__(b))

# 默认情况下，自定义类的比较是判断对象id是否相同
# a == b 等价于 a is b
# 只能比较相同，不能比较大小，其他均为None