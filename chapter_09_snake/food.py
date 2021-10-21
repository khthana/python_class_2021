from turtle import Turtle
import random


# class Food inherit มาจาก Turtle
# class Food ทำหน้าที่สร้างอาหาร เมื่อถูกกินจะสุ่มไปอยู่ที่อื่นแทน
class Food(Turtle):

    # constructor ของ class ทำหน้าที่
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
