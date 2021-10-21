from turtle import Turtle

# จะนำโปรแกรมจาก snake_game1 มาสร้างเป็น class
# จะสร้าง Class จำนวน 3 Class คือ snake, Food และ Scoreboard

# สร้างค่าคงที่ สำหรับใช้งาน
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# TODO : สร้าง Class snake โดยมี method 1) constructor 2) create 3) move_forward
#
# โดยงูจะเคลื่อนที่ไปเรื่อยๆ ทุกครั้งที่เรียกใช้ move_forward


class Snake:
    # ใน constructor จะมีการสร้าง งู ขึ้นมา จึงมีการสร้าง create_snake
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
