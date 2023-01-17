from math import *
from random import *
from turtle import *

shape('turtle')

speed(0)
penup()
goto(-1300, 0)
pendown()


def house(a):

    c = sqrt(2*a**2)
    b = c/2

    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    right(135)
    forward(b)
    right(90)
    forward(b)
    right(90)
    forward(c)
    right(135)
    forward(a)
    right(135)
    forward(c)
    left(45)


def random():
    while True:
        house(randint(10, 150))
        print('uwu')


random()
