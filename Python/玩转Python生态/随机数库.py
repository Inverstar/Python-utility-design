import random as r
import math
import time as t
print(t.time())
s = t.time()
print(t.asctime())
r.seed(s)
随机数 = r.random()
# [0,1)中随机浮点数 
print(随机数)

epi = r.uniform(math.e,math.pi)
print(epi)
# 从[a,b]中随机选数

print(r.randint(10,20))
#[int,int]

print(r.randrange(2,6,3))
# 同range()
c = ['李','康','智']
print(r.choice(c))

r.shuffle(c)
# 打乱的是原列表
print(c)
print(r.sample(c,3))
# 随机取出3个

# 设置随机种子
# 默认是系统时间
print(t.time())
print(t.ctime(t.time()))

