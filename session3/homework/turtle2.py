from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

x = 0
print(x)
for i in colors:
    setx(x)
    fillcolor(i)
    begin_fill()
    pencolor(i)
    forward(30)
    right(90)
    forward(60)
    right(90)
    forward(30)
    right(90)
    forward(60)
    right(90)
    end_fill()
    x += 30
    
print(x)   

mainloop()
