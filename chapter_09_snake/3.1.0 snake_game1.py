# เกม งู เริ่มจากความยาว 3 ส่วน
# เม็ดอาหารจะสุ่มครั้งละ 1 เม็ด ถ้างูกินอาหารก็จะยาวขึ้น 1
# จะแยกงานเป็น 2 ส่วน ส่วนที่ 1 ประกอบด้วย 3 ส่วนย่อย คือ 1) สร้างตัวงู 2) ทำให้งูเคลื่อนที่ 3) การควบคุมตัวงู
# ส่วนที่ 2 แบ่งเป็น 4 ส่วน 1) ตรวจจับการชนกับเม็ดอาหาร 2) นับคะแนน 3) ตรวจจับการชนผนัง 4) ตรวจจับการชนกับหางตัวเอง

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")   # ใส่ข้อความใน Title Bar
screen.tracer(0)                # ทำหน้าที่ปิดเปิด Animation

# TODO: 1) สร้างตัวงู
# ----------- v1 -------------------------
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_2.goto(-40, 0)

# ----------- v2 -------------------------
segments=[]
starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# TODO: 2) ทำให้งูเคลื่อนที่
# ----------- v1 -------------------------
# game_is_on = True
# while game_is_on:
#     for seg in segments:
#         seg.forward(20)
# จะเห็นว่าเส้นงูจะไม่ต่อเนื่อง ต้องใช้ turtle.tracer เพื่อปิด/เปิด animation

# ----------- v2 -------------------------
game_is_on = True
while game_is_on:
    screen.update()     # แสดงผล
    time.sleep(0.1)       # เพื่อลดความเร็ว
    # for seg in segments:
    #     seg.forward(20)
    #     #screen.update()     # แสดงผล

# ปัญหามีอยู่ว่าตอนเลี้ยวจะทำอย่างไร เพราะการเลี้ยวกล่องแรกไปกล่องหลังจะไปทิศทางเดิม
# ดังนั้นจะเปลี่ยนใหม่ โดยใช้วิธีเลื่อนจากกล่องหลังมาที่กล่องแรก
# โดยกล่องหลังจะเคลื่อนที่ไปทับกล่องด้านหน้า ยกเว้นกล่องแรก

    for seg_sum in range(len(segments)-1, 0, -1):
        new_x = segments[seg_sum-1].xcor()
        new_y = segments[seg_sum - 1].ycor()
        segments[seg_sum].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
