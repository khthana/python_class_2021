#---------------------------------------------------
#* ใน dictionary เราสามารถใช้ List หรือ Dictionary เป็น value ได้ 
#* เรียกว่า Nesting เช่น สมมติว่าเรามีเพื่อนอยู่หลายจังหวัด เราอาจทำแบบนี้ 

#* Nesting List in Dictionary
friend_list = {"Chiang Mai":['Mike','Peter'],
               "Nong Khai":['John','Mary']}

#* Nesting Dictionary in Dictionary
friend_contact = {"Chiang Mai":{'mike':'1234',
                                'peter':'2345'},
                  "Nong Khai":{'john':'3456',
                               'mary':'4567'
                               }
                 }

#| Ex 6.5 จากโปรแกรมต่อไปนี้ จงเขียนโปรแกรมในจุดที่ระบุ TODO

subject = { '01076031':'CALCULUS',
            '01076103':'PROGRAMMING FUNDAMENTAL',
            '01076104':'PROGRAMMING PROJECT',
            '01076112':'DIGITAL SYSTEM FUNDAMENTALS',
            '01076113':'DIGITAL SYSTEM FUNDAMENTALS IN PRACTICE',
            '01076118':'SYSTEM PLATFORM ADMINISTRATION'}

grade = {'A':4.0,'B+':3.5,'B':3.0,'C+':2.5,'C':2.0,'D+':1.0,'D':1.0,'F':0}

#TODO-1: สร้าง dictionary ของนักศึกษา {student_id:[student_name,year]}

#TODO-2: สร้าง function ชื่อ add_student โดยรับข้อมูลคือ student_id, student_name และ year (ชั้นปี)
#|       เช่น add_student('64010001','Tom Hanks',1)
#|       สร้าง function ชื่อ delete_student โดยรับข้อมูลคือ student_id 
#|       สร้าง function ชื่อ show_student โดยแสดงนักเรียนที่อยู่ใน dictionary 
#|
#|      Student ID  |  Student Name                | Year
#|       64010001   |  Tom Hanks                   |  1  
#|       64010002   |  Matt Damon                  |  2



