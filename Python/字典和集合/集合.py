"""
    set
    元素类型可以不同
    元素不可重复
    可以增删元素
    列表,字典,集合等可变数据类型不可为元素
    集合的作用是判断a 是否 in set

"""
print(set([]))
a = {1,2,2,(1,3)}
# print(a[1]) 集合无下标
# 自动去重
for x in a:
    print(x)
a = set("abc")
print(a)
# 字符串转集合单个字母
c = set({1:2,3:4})
print(c)
# 字典转集合只取键

a.add(3)
# a.add([3])
# 向集合a中添加3, 若有则不添加

a.clear()
# 清空集合

a = c.copy()
# 返回自身浅拷贝
print(a)
a.remove(3)
# 删除3, 若不存在则引发异常

a.update([1,2,3,4])
a.update((3,4,6))
a.update({1,6,7,8})
a.update({5:3,9:0})
# update 向集合中添加容器内元素
print(a)

# 集合运算
a = {1,2,3}
b = {3,4,5}
print(3 in a)
c = a|b #并集 
# a.update(b)
print(c)
c = a&b #交集
print(c)
c = a-b #差集，在a不在b
print(c)
c = a^b 
# 求a与b的对称差 (a|b) - (a&b)
print(c)

# a与b都是集合
a = {1,2}
b = {1,2,3}
print(a == b)#a与b元素是否一样
print(a != b)#a与b元素是否不一样
print(a <= b)# a是b的子集?
print(a < b)# a是b的真子集?

words = set([])
print(words)
while True:
    try:
        wd = input()
        words.add(wd)
    except:
        break
print(len(words))


