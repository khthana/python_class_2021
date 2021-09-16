
#| Ex 6.6 จากโปรแกรมต่อไปนี้ จงเขียนโปรแกรมในจุดที่ระบุ TODO

subject = { '01076031':'CALCULUS',
            '01076103':'PROGRAMMING FUNDAMENTAL',
            '01076104':'PROGRAMMING PROJECT',
            '01076112':'DIGITAL SYSTEM FUNDAMENTALS',
            '01076113':'DIGITAL SYSTEM FUNDAMENTALS IN PRACTICE',
            '01076118':'SYSTEM PLATFORM ADMINISTRATION'}

grade = {'A':4.0,'B+':3.5,'B':3.0,'C+':2.5,'C':2.0,'D+':1.0,'D':1.0,'F':0}

student = {}

def add_student(student_id, student_name, year):
    if student_id not in student:
        student[student_id] = [student_name,year]

def delete_student(student_id):
    del student[student_id]

def show_student():
    print('Student ID  |  Student Name                | Year')
    for std, std_detail in student.items():
        print(f"{std:^10}  |  {std_detail[0]:28}|{std_detail[1]:3}")

add_student()

#TODO-1: สร้าง dictionary ของการลงทะเบียน ชื่อ grade {student_id:{subject_id:grade }}
grade = {}

#TODO-2: สร้าง function ชื่อ regis_add โดยรับข้อมูลคือ student_id, subject_id
#|       เช่น regis_add('64010001','01076031')
#|       สร้าง function ชื่อ regis_delete โดยรับข้อมูลคือ student_id, subject_id
#|       สร้าง function ชื่อ grade_add โดยรับข้อมูลคือ student_id, subject_id, grade
#|       สร้าง function ชื่อ grade_show โดยรับข้อมูลคือ student_id โดยมีรูปแบบดังนี้

#|      Student ID : 64010001   Student Name : Tom Hanks
#|
#|      Subject ID  |  Subject Name                | Grade
#|       01076031   |  CALCULUS                    |  A
#|       01076103   |  PROGRAMMING FUNDAMENTAL     |  B+

"""
def regis_add(student_id, subject_id):
    if student_id not in student:
        print ('student not found')
    else:
        if (subject_id in grade[student_id]):
            print(f"{subject_id} already registered")
        else:
            grade[student_id]={subject_id}
""" 





