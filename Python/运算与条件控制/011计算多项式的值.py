#对于多项式f(x) = ax3 + bx2 + cx + d 和给定的a, b, c, d, x，计算f(x)的值。
#5b8d34c3d46a880e7dea0438b3ba722025b5deacb3453b829aec8767a2348e57
f = input().split()
x = eval(f[0])
a = eval(f[1])
b = eval(f[2])
c = eval(f[3])
d = eval(f[4])

print("%.7f"%(a*(x**3)+b*(x**2)+c*x+d))
