# เราได้เรียนเรื่องของ Class และ Object แล้ว
# จาก class Turtle() คราวนี้เราจะสร้างหลายๆ Object

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# tim = Turtle()      # เต่าแต่ละตัว จะเรียกว่า Instance
# tom = Turtle()      # ซึ่งจะเป็นอิสระต่อกัน โดยลักษณะของแต่ละตัวจะเรียกว่า state

user_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]   # ตำแหน่งของ Screen จะถือว่าตรงกลางคือ 0,0
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
