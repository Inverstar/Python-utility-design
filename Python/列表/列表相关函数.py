a = []
c = [12,1]
c.append(a)
# 无限叠加???
def 无尽(c):
    for i in c:
        if i == c:
            无尽(i)
        else:
            print(i)
# 无尽(c)
print(c)
a.extend(c)
a.insert(2,2)
print(a)
a.remove(1)
a.reverse()
# 逆转列表
print(a)
try:
    print(a.index(1))
except Exception as e:
    print(e)

#列表映射
#map(function, sequence) 可将序列映射到另一个序列, 返回一个延时求值对象, 可转换为容器
def f(x):
    return x**x
a = map(f,[1,2,3])
print(tuple(a))
print(list(a))
# 延时操作在使用时激活, 之后失效
# 所以最好结合lambda来用
a = list(map(lambda x: x*[x**x],[2,3,4]))
print(a)

#map处理输入
# x,y,z = map(int,input().split())
# print(x,y,z)

#列表过滤
#filter(function,sequence) 抽取序列中返回值为True的元素
print(list(filter(lambda x: x%2 == 0,[1,2,3,4])))