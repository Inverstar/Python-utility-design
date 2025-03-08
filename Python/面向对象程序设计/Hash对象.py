# 可哈希才能作为字典的键和集合元素
# hash(x) 有定义即可x可哈希
# x 是整型常量，则结果为x
# x.__hash__()
print(hash(object))

# hash(a) == hash(b) 但是 a != b 则a，b可以处于同一集合

# hash值
# 自定义对象的哈希值根据id计算得到，只要a is b不成立则不同
# 可以重写自定义类的__hash__()方法

# a==b等价于a.__eq__(b)
# 自定义类的__eq__函数是根据id判断
# 如果重写它，__hash__成员函数自动设置为None，对象不可哈希
# 但是重写__hash__不会影响__eq__,此时可能出现hash相同但id不同

print(id(object))


