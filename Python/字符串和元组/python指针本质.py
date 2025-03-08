x = 123
y = int
b = isinstance(x,y)
#   判断x是不是类型y
#   类型判断函数
print(b)
print(id(y),id(int))

c = (1,2,)
c = (1,2)
# 圆括号括起来的就叫元组tuple
print(len(c))

# 所有可赋值, 在=左边的即是指针
# 变量=指针 指向内存单元位置

# is 与 == 的区别
a = 2
b = a # 使得a与b指向同一个地方
print(a is b)
# Ture说明指向了同一个地方
print(a == b)
# Ture说明存放的东西相同,但地方未必相同
# 对数字型与字符串和元组而言, is没有意义
# 对list, dict, set则需要关注数据变化
a = [1,2,3,4]
b = [1,2,3,4]
print(a[0] is b[0])
print(a is b)
# python中常量数据唯一, 所以指向1的指针所指向的地址相同
print(id(a),id(b))
