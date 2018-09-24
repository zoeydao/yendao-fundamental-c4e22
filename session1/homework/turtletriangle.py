import turtle
triangle = turtle.Turtle()
triangle.begin_fill()
for i in range(3):
    triangle.color("yellow")
    triangle.pencolor("green")
    triangle.forward(90)
    triangle.left(120)
triangle.end_fill()
turtle.done()