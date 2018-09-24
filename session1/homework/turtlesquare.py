import turtle
sq = turtle.Turtle()
sq.begin_fill()
for i in range(4):
   sq.color("yellow")
   sq.pencolor("green")
   sq.forward(90)
   sq.left(90)
sq.end_fill()
turtle.done()