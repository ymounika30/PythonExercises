import turtle
my_window=turtle.Screen()
my_window.bgcolor("black")
my_pen=turtle.Turtle()
my_pen.color("white")
def my_sqrfunc(size):
    for i in range(4):
        my_pen.fd(size)
        my_pen.left(90)
        size=size-5
my_sqrfunc(146)
my_sqrfunc(126)
my_sqrfunc(106)
my_sqrfunc(86)
my_sqrfunc(66)
my_sqfunc(46)
my_sqrfunc(26)
