# 字符串编码在内存中是unicode
print(ord('a'))
print(chr(22900))
print("%d"%1,15)
a = 1 
print(f"{a}")
x = "Hello {0} {1:10},you get ${2:0.4f}"\
.format("Mr.","Jack",3.2)
print(x)
x = "Hello {0} {1:^10},you get ${2:0.4f}"\
.format("Mr.","Jack",3.2)
print(x)
"""
    format()函数的语法规则
    {1:8}
    {序号:填充符 对齐符 宽度.精度 类型}
    宽度: 最小宽度, 不足补空格
    对齐符: >右对齐 左填充
            <左对齐 右填充 默认
            ^居中 

"""
