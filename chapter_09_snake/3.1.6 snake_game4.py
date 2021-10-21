# เกม งู เริ่มจากความยาว 3 ส่วน
# เม็ดอาหารจะสุ่มครั้งละ 1 เม็ด ถ้างูกินอาหารก็จะยาวขึ้น 1
# จะแยกงานเป็น 2 ส่วน ส่วนที่ 1 ประกอบด้วย 3 ส่วนย่อย คือ 1) สร้างตัวงู 2) ทำให้งูเคลื่อนที่ 3) การควบคุมตัวงู
# ส่วนที่ 2 แบ่งเป็น 4 ส่วน 1) ตรวจจับการชนกับเม็ดอาหาร 2) นับคะแนน 3) ตรวจจับการชนผนัง 4) ตรวจจับการชนกับหางตัวเอง

from classSnake3 import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")  # ใส่ข้อความใน Title Bar
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()  # TODO สร้าง Score board

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: ตรวจจับการชนกันระหว่างงู กับ อาหาร
    # ใน Tuttle จะมี method ชื่อ distance โดยจะส่งค่าระหว่าง x,y กับ Turtle
    # ถ้าเราเช็คระยะระหว่าง Turtle กับ food ถ้าน้อยกว่าที่กำหนด ก็จะถือว่าชนกันได้

    if snake.head.distance(food) < 15:
        food.refresh()

        # TODO: เพิ่มความยาวหาง
        snake.extend()

        # TODO: สร้างคะแนน (Scoreboard) โดยจะสร้างใน Class
        scoreboard.increase_score()

    # TODO: ตรวจจับการชนกับกำแพง โดยขอบเขตของ Screen คือ -300 -> 300
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # TOD0: ตรวจว่าชนกับหางตัวเองหรือไม่ ตรวจสอบว่าหัวใกล้กับงูส่วนใดหรือไม่ ยกเว้นส่วนหัว
    # Code นี้ ยังไม่ Optimize เพราะใช้ Slicing ได้
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
