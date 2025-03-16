#编写程序，计算下列分段函数y=f(x)的值。
#b879aa0de10d2be27e3b34b2f3f33fc38c6cc306e0c67d0cf48c0ae35f67483b
x = float(input())
if 0 <= x < 5:
    y=-x+2.5
elif 5 <= x < 10:
    y=2-1.5*(x-3)*(x-3)
else:
    y=x/2-1.5
print("%.3f"%y)