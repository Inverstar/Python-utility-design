import copy
a = [1,2,3,4]
b = a[:]
# b 是 a 的 拷贝
print(b)

# 列表深拷贝
# 导入copy库
a = [1,2,[1]]
b = copy.deepcopy(a)
# b = a[:]
print(b)
a[2].append(1)
print(b)

# 互转
a=list("hello")
a = []
a = "".join(a)
print(a)
print(''.join(a))
a = tuple('heoo')
print(''.join(a))
