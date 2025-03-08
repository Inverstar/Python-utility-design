#将正整数n表示成一系列正整数之和
def ways(n,m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    w = ways(n,m-1)
    if n >= m:
        w += ways(n-m,m)
    return w
a = int(input())
print(ways(a,a))