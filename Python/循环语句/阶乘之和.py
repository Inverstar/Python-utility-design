n = int(input())
s, f = 0, 1
for i in range(1,n+1):
    f *= i
    s += f
    print(s)