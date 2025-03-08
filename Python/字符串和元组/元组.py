# 元组不能修改, 由数个逗号分隔的值组成, 括号可加可不加
"""
    不可增删元素
    不可赋值元素
    不可修改顺序
"""
# 元组：指针或常量，常量不可变，指针指向可变

t = 1,2,1
print(t)
# t 是元组 tuple
u = t,1,2,3
print(t,u)
print(u[0][1])
print(u[0])

# 元组的元素本身不可变, 但元素的内容可能修改
v = ('hello',[1,2,3],[3,2])
#v[1] = 32 # 报错 'tuple' object does not support item assignment
v[1][0] = 'w'
print(v)
print(len(v))
# 元组元素都是指针, 指向的地址不变

empty = () #空元组
singleton = 'hello', #逗号意味元组,无则字符串
print(len(singleton))
print(singleton)

#元组下标访问与切片
tuple1 = 'Google','Baidu','Sougo'
print(tuple1[:])
print(tuple1[::])
print(tuple1[::-1])

#元组之间可以连接组合
tup1,tup2 = (12,22),('ad','nv')
# 居然正常赋值了,,,没有看作为一个元组
print(tup1,tup2)
tup3 = tup1 + tup2
print(tup3)
tup3 += 10, #元组只能链接元组
print(tup3)

x = (1,2,3) * 3 # *像是连加号
print(x)
for i in x:
    print(i,end = '')
b = x
print('\n',b is x)
x += (100,)
print(x is b)

# b = ('a',) #python 中哪些元素之间可比较大小?
print(x>b) # 元组比较是对应元素比大小, 若出现两元素不可比, 则报错

def tup_test():
    # a是指针, 所以给b的是它的地址
    a = [1,2,3]
    b = (a,a)
    b[0][1] = 100
    print(a,b)
tup_test()