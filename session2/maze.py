from turtle import *

d = 10
for _ in range(20):
    forward(d)
    d = d + 10 #d += 10
    left(90)
forward(d)   
mainloop()