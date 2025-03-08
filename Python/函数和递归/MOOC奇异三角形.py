import turtle  # 画图用turtle包
def strange(n, size):  
    # n为阶数，size为长度，从当前起点出发
    if n == 0:
        for angle in [0, -120, -120]:  # 对列表中的每个元素angle
            turtle.left(angle)  # 笔左转angle度，turtle.lt(angle)也行
            turtle.fd(size)  # 笔沿当前方向前进size
        turtle.left(-120)  # 调整方向对准下一个边
    else:
        for angle in [0, -120, -120]:  # 对列表中的每个元素angle
            turtle.left(angle)  # 笔左转angle度，turtle.lt(angle)也行
            strange(n - 1, size / 2)
            turtle.fd(size)
        turtle.left(-120)  # 调整方向对准下一个边
def n阶奇异(n):
    turtle.setup(1000, 1000)
    turtle.speed(0)  # 画快点
    turtle.penup()  # 抬起笔
    turtle.goto(-400, -300)  # 把笔移动起始位置
    turtle.pendown()  # 放下笔
    turtle.pensize(2)  # 笔的粗细为1
    turtle.left(60)  # 调整起始方向到60度
    strange(n, 800)  # 绘制长度为800，阶为level的奇异三角形
    turtle.done()  # 保持绘图窗口
n阶奇异(6)