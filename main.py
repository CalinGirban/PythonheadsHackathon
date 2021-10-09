from turtle import *
p=getscreen()
penup()
setpos(-100,-250)
pendown()
pensize(4)
for x in range(4):
    if x%2==0:
        forward(250)
    else:
        forward(50)
    left(90)
pensize(2)
penup()
setpos(-100,-233)
pendown()
forward(250)
penup()
setpos(-100,-217)
pendown()
forward(250)
penup()
