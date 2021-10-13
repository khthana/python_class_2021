import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


# TODO ปรับสีให้เป็น Random

def random_color():
    r = random.randint(255)
    g = random.randint(255)
    b = random.randint(255)
    color = (r, g, b)
    return color


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
