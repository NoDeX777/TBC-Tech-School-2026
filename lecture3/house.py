from turtle import end_fill
from turtle import begin_fill
from turtle import *
def draw_square(clr,size):
    color(clr)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()
def draw_triangle(clr,size):
    color(clr)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()
def draw_house(x,y,clr,size):
    penup()
    goto(x,y)
    pendown()
    draw_square(clr,size)
    penup()
    goto(x,y+size)
    pendown()
    draw_triangle("orange",size)
draw_house(-200,-200,"red",100)
done()