from turtle import *

length = 100
num_sides = 3

#triangle
pencolor("blue")
left(60)
for _ in range(num_sides): 
    forward(length)
    right(360/num_sides)
#square
pencolor("red")
left(30)
num_sides += 1
for _ in range(num_sides): 
    forward(length)
    right(360/num_sides)
#pentagon
pencolor("blue")
left(18)
num_sides += 1
for _ in range(num_sides): 
    forward(length)
    right(360/num_sides)
#hectagon
pencolor("red")
left(12)
num_sides += 1
for _ in range(num_sides): 
    forward(length)
    right(360/num_sides) 

right(120)
fillcolor("red")

mainloop()