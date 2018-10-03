from turtle import *

length = 100
num_sides = 3

degrees = [60,30,18,12,8]
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

i = 0
for degree in degrees:
    pencolor (colors[i])
    left(degree)
    for _ in range(num_sides): 
        forward(length)
        right(360/num_sides)   
    num_sides += 1
    i += 1
    
mainloop()
