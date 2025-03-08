# 你买了一箱n个苹果，很不幸的是买完时箱子里混进了一条虫子。虫子每x小时能吃掉一个苹果，假设虫子在吃完一个苹果之前不会吃另一个，那么经过y小时你还有多少个完整的苹果？
#c3d33195a6f56299a5ee91ccac20f16011fd0ab0abe27f3eb919e23f156f7caf
s = input().split()
n = int(s[0])
x = int(s[1])
y = int(s[2])
if y == 0:
    print(n)
elif n>0:
    if y<x:
        print(n-1)
    else:
        if y%x == 0:
            if n-y/x < 0:
                print(0)
            else:
                print(n-y//x)
        else:
            if n - y//x - 1<0:
                print(0)
            else:
                print(n-y//x-1)
else:
    print(0)