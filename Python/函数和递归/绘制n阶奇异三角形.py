import turtle
def 奇异三角形(n,size):
    if n == 0:
        for angle in [60,-120,-120]:
            turtle.left(angle)
            turtle.fd(size)
    else:
        pos = turtle.pos()
        奇异三角形(n-1,size/2)
        turtle.penup()
        turtle.goto(pos)
        turtle.right(120)
        turtle.fd(size/2)
        turtle.right(60)
        turtle.pendown()
        奇异三角形(n-1,size/2)
        turtle.penup()
        turtle.goto(pos)
        turtle.right(180)
        turtle.fd(size/2)
        turtle.pendown()
        奇异三角形(n-1,size/2)
def n阶三角形(n):
    turtle.setup(800,800)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300,-200)
    turtle.pendown()
    turtle.pensize(2)
    奇异三角形(n,600)
    turtle.done()
n阶三角形(6)