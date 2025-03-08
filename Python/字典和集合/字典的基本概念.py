d = {1 : 'a'}
# 字典的每个元素都由键:值组成
# 值可以是指针, 可被赋值
# 键唯一
# 键必须是不可变数据类型, 字符串,数字,元组 而集合，列表，字典为可变数据类型
print(d[1])
d[1] = 'ok'
# 有则改之, 无则加典!
d[2] = d[1]
# 传值不传址 ?
print(d)
d[1] = '111'
del d[1]
print(d)
print(2 in d) # in判断键是否存在

d[1] = print(d.get(1,-1))
print(d.get(1))
# get(键, 值), 返回键对应的值,没有返回值
for i in d :
    print(i, d[i])
for i in enumerate(d):
    print(d[i[1]])

# 字典的键不可重复
a = 1
b = 1
d = {a:60,b:30,1:20}
# 只有最后一个起作用
print(d)

# 利用列表构造字典
list1 = [('1',1),('2',2)]
d = dict(list1)
print(d)

d = dict(n=12,a=11,c=11)
print(d)

dict1 = {1:3,2:4}
print(dict1.setdefault(3))
print(dict1)
k = list(dict1.values())
print(k[0])

