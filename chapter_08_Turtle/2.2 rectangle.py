from turtle import Turtle
import random

tim = Turtle()


# TODO: เขียนโปรแกรมให้วาดรูป 4 เหลี่ยม
def draw_rectangle():
    tim.forward(100)
    tim.color('blue')
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)


draw_rectangle()
