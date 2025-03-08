"""
    常数复杂度 O(1)
    对数复杂度 O(log(n))
    线性复杂度 O(n)
    多项式复杂度 O(n**k)
    指数复杂度 O(a**n)
    阶乘复杂度 O(n!)

"""
s = "1"

# 顺序查找 O(n)
# 插入与选择 O(n**2)
# 快速排序 O(n*log(n))
# 二分查找 O(log(n))

# in 在列表与{字典,集合}的区别
a = 1
b = {1:2}
# b是列表,字符串,元组 O(n)
# b是字典,集合, O(1)
print(a in b)

# O(1) 集合字典增删查找, 列表字符串元组下标访问
# O(n) 列表\元组查找(in,index), 插入insert删除remove元素 计数count
# O(nlogn) python自带排序 sort, sorted
# O(logn) 在排好序的列表或元组二分查找


