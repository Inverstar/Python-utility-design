#字符串 用三种引号括起来
print("this\
    换行\
        快乐")
#三双引号字符串可以包含换行符, 制表符及其他特殊字符
str = """   \n 你看懂了\t吗?"""
#双索引下标a[-1]=a[n-1]
print(str[2])

a = "ABCD"
b = "1234"
a = a + b
print(a)
a += a[1]
print(a)
#可以直接修改字符串, 但不能对引用进行操作
#a[2] = 'k'#object does not support item assignment
print(a[2])
# in not in 判断子串
a = "hello"
b = "123"
print('1'in b)
