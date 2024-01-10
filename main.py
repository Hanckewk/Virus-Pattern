import turtle
from turtle import *
speed(0.3)
color('cyan')
bgcolor('black')
b = 20

while b > 0:
    left(b)
    forward(b*3)
    b = b-1
    left(b)
    forward(b*4)
    left(b)
    forward(b * 4)
    
if 'name' != 'main':
    turtle.done()