#鸡尾酒疗法
#ae8092b8c05be0fe13fff613a51db1a81cc502e6c51440c7d0993cb1ffec12f3
n = int(input()) - 1
s = input().split()
s = eval(s[1]+'/'+s[0])
while n:
    n -= 1
    x = input().split()
    x = eval(x[1]+'/'+x[0])
    if x - s > 0.05:
        print("better")
    elif s - x > 0.05:
        print("worse")
    else:
        print("same")
