a = 12 #变量与注释
k = 12.2E3 #支持科学记数法
b = a
print( k )
'''
大小字母或下划线开头
无空格, 长度无限
预留字
赋值语句
    变量 = 表达式
'''
a, b = "he", 12
print(a,b)
a,b = b,a 
a = b = c = [] #居然允许连续赋值
print(id(a),id(b))
print(id(a)==id(b))#说明a,b指向同一地址
b.append(1)
print(a,b,id(b),c)
print(id(1))
#程序顶格书写!