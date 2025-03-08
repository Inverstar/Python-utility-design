#bool
#python支持连续比较，但是不建议这样使用。。。
# chr() ord()
# 算术>关系>逻辑
a = 4
print()
print(2<a<6<8)
print(1<2<a)
print(2<a==4<6)
print(2<a>5)
print(1==True)
print(0==False)
print(-1==False)
print()
#关系运算符也能比较字符串, 按字典序, 小写大于大写
print('a'>'A')

#逻辑运算符
n = 4
print(n>4 and n<5)
print(5 or False)   #输出了5
print(4 and True)   #True

print(''==False) #0或空相当于False但只有0等于False
print(True == 1) #非0数与非空结构相当于True, 除1外都不等于True
print(''==0)
print(0==False)

#在逻辑表达式里面, 值可以是相当于False或True的东西

print(not '')
#not > and > or 优先级

#短路计算