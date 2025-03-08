x = 4
def f0():
    print(x)
def f1():
    x = 8
    print("f1:",x)
def f2():
    global x
    print("f2:",x)
    x = 5
    print("f2:",x)
def f3():
    
    x = 9
    print(x)
    #f3会出错, 后面的赋值语句使得x当作了局部变量
f0()
f1()
print(x)
f2()
print(x)
f3()