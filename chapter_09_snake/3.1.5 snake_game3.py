# เกม งู เริ่มจากความยาว 3 ส่วน
# เม็ดอาหารจะสุ่มครั้งละ 1 เม็ด ถ้างูกินอาหารก็จะยาวขึ้น 1
# จะแยกงานเป็น 2 ส่วน ส่วนที่ 1 ประกอบด้วย 3 ส่วนย่อย คือ 1) สร้างตัวงู 2) ทำให้งูเคลื่อนที่ 3) การควบคุมตัวงู
# ส่วนที่ 2 แบ่งเป็น 4 ส่วน 1) ตรวจจับการชนกับเม็ดอาหาร 2) นับคะแนน 3) ตรวจจับการชนผนัง 4) ตรวจจับการชนกับหางตัวเอง

from classSnake2 import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")  # ใส่ข้อความใน Title Bar
screen.tracer(0)

snake = Snake()

# TODO : ใช้ listen method รับคีย์บอร์ด และ เรียกใช้ method up, down, left, right เพื่อตั้งทิศทางใหม่
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

screen.exitonclick()
