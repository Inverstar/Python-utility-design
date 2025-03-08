# numpy多维数组库
# 速度比多维列表快
# 支持向量与矩阵运算
# 元素类型相同
import numpy as np
from regex import D
print(np.array([1,2,3]))
print(np.arange(1,9,2))
print(np.linspace(1,10,4))
print(np.random.randint(10,20,[2,3]))
# [10,20)
a = np.zeros(3)
print(a)
a = np.zeros((2,3),dtype=int)
print(a)

# numpy常用属性与函数
b = np.array([i for i in range(12)])
a = b.reshape((3,4))
print(a)
print(len(a)) #a的长度
print(a.size) #a的元素个数
print(a.ndim) #a的维度
print(a.shape) #a的形状
print(a.dtype) #a的元素类型



