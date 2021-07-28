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

#-------------------------------------------
#* if condition:
#*     statement
#* elif condition:
#*     statement
#* else:
#*     statement
#*
#* จะใช้กรณีที่มีหลายเงื่อนไข 
* operator ที่ใช้ใน condition ==, !=, >, >=, <, <=
"""



num = 0
if num == 0:
    print("Zero Number")
elif num < 0:
    print("Negative number")
else:
    print ("Positive Number")

