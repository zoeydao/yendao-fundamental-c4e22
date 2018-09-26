from turtle import *

length = 100
num_sides = 3

#triangle
pencolor("blue")
left(60)
for _ in range(3):
    forward(length)
    right(360/num_sides)
#square
pencolor("red")
left(30)
num_sides = 4
for _ in range(4): 
    forward(length)
    right(360/num_sides)
#pentagon
pencolor("blue")
left(18)
num_sides = 5
for _ in range(5): 
    forward(length)
    right(360/num_sides)
#hectagon
pencolor("red")
left(12)
num_sides = 6
for _ in range(6): 
    forward(length)
    right(360/num_sides)   

right(120)
fillcolor("red")

mainloop()