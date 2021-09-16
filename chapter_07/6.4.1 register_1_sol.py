subject = { '01076031':'CALCULUS',
            '01076103':'PROGRAMMING FUNDAMENTAL',
            '01076104':'PROGRAMMING PROJECT',
            '01076112':'DIGITAL SYSTEM FUNDAMENTALS',
            '01076113':'DIGITAL SYSTEM FUNDAMENTALS IN PRACTICE',
            '01076118':'SYSTEM PLATFORM ADMINISTRATION'}

grade = {'A':4.0,'B+':3.5,'B':3.0,'C+':2.5,'C':2.0,'D+':1.0,'D':1.0,'F':0}

#TODO-1: สร้าง dictionary ของนักศึกษา ชื่อ student {student_id:[student_name,year]}
student = {}

#TODO-2: สร้าง function ชื่อ add_student โดยรับข้อมูลคือ student_id, student_name และ year (ชั้นปี)
#|       เช่น add_student('64010001','Tom Hanks',1)
#|       สร้าง function ชื่อ delete_student โดยรับข้อมูลคือ student_id 
#|       สร้าง function ชื่อ show_student โดยแสดงนักเรียนที่อยู่ใน dictionary 
#|
#|      Student ID  |  Student Name                | Year
#|       64010001   |  Tom Hanks                   |  1  
#|       64010002   |  Matt Damon                  |  2

def add_student(student_id, student_name, year):
    if student_id not in student:
        student[student_id] = {student_name:year}

def delete_student(student_id):
    del student[student_id]

def show_student():
    print('Student ID  |  Student Name                | Year')
    for std, std_detail in student.items():
        print(f"{std:^10}  |  {std_detail[0]:28}|{std_detail[1]:3}")

add_student('64010001','Tom Hanks',1)
add_student('64010002','Jennifer Aniston',2)
show_student()
print('delete')
delete_student('64010002')
show_student()



