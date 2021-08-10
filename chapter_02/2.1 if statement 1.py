#-------------------------------------------
#* คำสั่ง if  ใช้ในการกำหนดเงื่อนไขการทำงาน
#-------------------------------------------

#-------------------------------------------
#* if condition:
#*    statement
#* จะใช้กรณีที่ตรงตามเงื่อนไข แล้วทำคำสั่งใน statement
#-------------------------------------------

### ตัวอย่าง : สมมติว่าในสวนสนุก เด็กจะได้ลด 50 ถ้าสูง<120

height = int(input("What is your height in cm. :"))
if height > 120:
    print("You can enter theme park")

#-------------------------------------------
#* if condition:
#*    statement1
#* else:
#*    statement2
#*
#* จะใช้ในกรณีที่ถ้าตรงตามเงื่อนไข จะทำตาม statement 1
#* แต่ถ้าไม่ตรง จะทำตาม statement2
#-------------------------------------------

num = int(input("Enter your number (integer): "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

#| Ex.2.1 1 จงเขียนโปรแกรมรับค่าของตัวเลข 1 ค่า (x) จากคีย์บอร์ด
#|          และทดสอบว่าเป็นเลขที่หารด้วย 5  ลงตัว หรือไม่ ตัวอย่าง
#|              Enter x: 10
#|              10 is divisible by 5.
#|              Enter x: 11
#|              11 is not divisible by 5.

#-------------------------------------------
#* if condition1:
#*     statement1
#* elif condition2:
#*     statement2
#* else:
#*     statement3
#*
#* จะใช้กรณีที่มีหลายเงื่อนไข ถ้าไม่ตรงกับเงื่อนไขที่ 1 
#* ก็จะไปตรวจสอบในเงื่อนไขที่ 2 ต่อไป 
#-------------------------------------------

### ตัวอย่าง : ในสวนสนุกแห่งหนึ่งมีอัตราการเข้าชมต่างกันตามอายุ
### ถ้าต่ำกว่า 4 ขวบ ฟรี
### อายุ 4-18 = 25 บาท
### อายุ 18-65 = 40 บาท
### อายุ > 65 = 20 บาท
### จงเขียนโปรแกรมรับอายุแล้วคำนวณจำนวนเงิน

age = int(input("Enter your age : "))

if age <= 4:
    price = 0
elif age <= 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is {price}.")

#-------------------------------------------
#* หรือจะเขียนแบบนี้ก็ได้
#-------------------------------------------

age = int(input("Enter your age : "))

if age <= 4:
    price = 0
if 4 < age <= 18:
    price = 25
if 18 < age <= 65:
    price = 40
if age >= 65:
    price = 20

print(f"Your admission cost is {price}.")



#| Ex.2.2 จงเขียนโปรแกรมรับข้อมูลจำนวน 2 ค่า คือ
#| คะแนน midterm และ final
#| ถ้าคะแนนรวมกัน > 50 แสดง pass ถ้าต่ำกว่าแสดง fail

m_score = int(input("Enter midterm score:"))
f_score = int(input("Enter final score:"))

#-------------------------------------------
#* operator ที่ใช้ใน condition ==, !=, >, >=, <, <=
#-------------------------------------------

### ตัวอย่าง : สมมติว่าการโอนเงินมีค่าธรรมเนียม 
###          0-5000 ไม่มีค่าธรรมเนียม
###          5000-30,000        2 บาท
###          30,000-100,000     5 บาท
###          >100,000           10 บาท 
###          จงหาจำนวนเงินที่ต้องจ่ายในการโอน


amount = int(input("Enter amount of transfer money: "))
fee = 0
if amount<=5000:
    fee=0
elif 5000 < amount <= 30000:
    fee=2
elif 30000 < amount <= 100000:
    fee=5
else:
    fee=10

print(f"Transfer fee = {fee}.")

#| Ex.2.3 จงเขียนโปรแกรมรับข้อมูลความเร็ว
#| ถ้าน้อยกว่า 45 แสดงผล slow speed
#| ถ้าระหว่าง  45 -> 90 แสดงผล moderate speed
#| ถ้ามากกว่า 90 ให้แสดงผล fast speed

speed = input("Enter speed:")



