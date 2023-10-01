import turtle as t

t.bgcolor('white')
t.pencolor('green')
t.width(3)
t.speed(100)

def form(x):
    t.circle(100, x)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(-100, x)

def leaf():
    for i in range(0, 150, 10):
        form(i)

leaf()
t.setheading(90)
leaf()
t.setheading(180)
leaf()
t.setheading(270)
leaf()
t.exitonclick()