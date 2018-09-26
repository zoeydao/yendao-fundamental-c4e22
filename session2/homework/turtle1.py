from turtle import *

pencolor("red")
fillcolor("red")
length = 80
angle = 150

for i in range(4):
    left(angle)
    forward(length)
    left(60)
    forward(length)
    left(120)
    forward(length)
    left(60)
    forward(length)
    angle=30

mainloop()