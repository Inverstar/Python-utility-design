#科赫曲线
import turtle
def snow(n,size):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            snow(n-1,size/3)
def 曲线(n):
    turtle.setup(800,600)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(3)
    snow(n,600)
    turtle.done()
def 雪花(n):
    turtle.setup(800,800)
    turtle.speed(10000)
    turtle.penup()
    turtle.goto(-300,200)
    turtle.pendown()
    turtle.pensize(2)
    snow(n,600)
    turtle.right(120)
    snow(n,600)
    turtle.right(120)
    snow(n,600)
    turtle.done()

雪花(5)
