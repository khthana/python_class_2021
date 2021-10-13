from turtle import Turtle, Screen

screen = Screen()

tim = Turtle()


# Function as Input
# https://docs.python.org/3/library/turtle.html#turtle.listen

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
