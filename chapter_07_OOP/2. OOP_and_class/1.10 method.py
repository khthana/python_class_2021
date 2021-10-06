# เราสามารถเพิ่มฟังก์ชันที่ใช้ในาการจัดการข้อมูลของ class เรียกว่า method

class Student:
    # method __init__ เป็น method ที่จะถูกเรียกใช้โดยอัตโนมัติเมื่อมีการสร้าง object
    # มักใช้ในการกำหนดค่าเริ่มต้นของ object
    # การอ้างถึงตัวแปร (attribute) ใน class จะมีคำว่า self นำหน้าเสมอ

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.year = 1  # default value
        self.peer_mentor = 0  # พี่รหัส
        self.peer_mentee = 0  # น้องรหัส

    def upgrade(self):  # เลื่อนชั้นปี
        self.year += 1

    def set_mentor(self, student):
        self.peer_mentor = student
        student.peer_mentee = self

# การเรียกใช้ method จะใช้ object.method_name

std1 = Student('64015001', 'Tom')
print(std1.year)
std1.upgrade()
print(std1.year)
std2 = Student('63015200', 'Peach')
std1.set_mentor(std2)
print(std1.peer_mentor)
print (f"พี่รหัสของ {std1.student_id} คือ {std1.peer_mentor.student_id}")

print (f"น้องรหัสของ {std2.student_name} คือ {std2.peer_mentee.student_name}")

