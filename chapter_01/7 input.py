"""
* การรับค่าข้อมูลที่เป็นสตริง
 <variable> = input("text")

* การรับค่าข้อมูลที่เป็นตัวเลข 
 <variable> = int(input("text")) หรือ <variable> = float(input("text"))
"""

name = input("What’s you name : ")
print("Your name is :",name)
name = input("What’s you name : ")
print("Your name is :",name)

width = int(input("Enter height :"))
print("height = ",height)

#* จงเขียนโปรแกรม คำนวณพื้นที่สี่เหลี่ยมผืนผ้า โดยกำหนดตัวแปร
#* width และ height โดยรับค่าจาก keyboard 
#* การแสดงผลให้ใช้ f string ช่วย

"""
* การ Input ทีละหลายค่า 
a,b,c = input().split() อ่าน string
x,y = [int(e) for e in input().split()]
a,b,c = [float(e) for e in input().split()]
"""

#|Ex. อ่านจำนวนจริง 5 จำนวน คั่นด้วยช่องว่าง
#|    คำนวณค่าเฉลี่ยของจำนวนทั้งห้า แล้วแสดงค่าเฉลี่ย



#| Ex. รับข้อมูล 3 ตัว a, b กับ c คั่นด้วยช่องว่าง
#|     a และ b เป็นตัวอักษรตัวเดียว ส่วน c เป็นจำนวนเต็ม
#|     ให้แสดงตัวอักษรใน a ต่อกับตัวอักษรใน b แล้วตามด้วย c
#|     แล้วตามด้วยตัวอักษร a+b จำนวน c ชุด
#|     เช่น a b 5 -> ab5ababababab
