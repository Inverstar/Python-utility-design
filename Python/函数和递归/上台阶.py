def ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return ways(n-1)+ways(n-2)
print(ways(4))
#走台阶, n级, 每步一级或2级, 共多少种走法?