# การเขียน Class มักขึ้นต้นคำเป็นตัวใหญ่ แล้วตามด้วยตัวเล็ก (Pascal case) เช่น
class User:
    pass


# จาก Class เราสร้าง object ได้ตามนี้
user_1 = User()
user_1.id = "001"
user_1.name = "Somchai"
print(user_1.id)
print(user_1.name)


class User2:
    # __init__ ใช้ในการ Initialize Object เป็น Fn ที่จะถูกเรียกใช้เมื่อสร้าง class
    def __init__(self):
        print("New student being created.....")


user_2 = User2()
user_2.id = "002"
user_2.name = "Sombat"
print(user_2.id)
print(user_2.name)


# เราสามารถกำหนด Attribute ของ Object ตั้งแต่ตอนสร้างก็ได้ เรียกว่า Constructor
# การอ้างถึง attribute หรือ ตัวแปร ภายใน class เราจะขึ้นต้นด้วย self.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.year = 1       # default value


std1 = Student('001', 'Tom')
print(std1)
