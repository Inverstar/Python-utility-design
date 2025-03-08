list1 = [1,2]
del list1[1]
# del list1[3]
list1 += [100,1]
list1.append([100,1]) #添加1个元素
print(list1)

# 列表的 += 与 + 不一样
b = a = [1,2]
a += [3]
a += b
print(a,b)
# a的地址不变, 所以b也会变化
a = a + [1,2]
# a被重新赋值,地址改变, b无影响

#列表乘法
a = [1,2]
c = a * 3 #将结果赋给c
c = [a] * 3 #将a的地址给c
a.append(3)
print(c)

a = [[0]]*2 + [[0]]*2
a[0][0] = 5
print(a)

#列表的切片
#列表的遍历
for x in a:
    a[1] = x
    print(a)
#列表比大小