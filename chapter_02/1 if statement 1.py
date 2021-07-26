'''
คำสั่ง if  ใช้ในการกำหนดเงื่อนไขการทำงาน 

if condition:
    statement

if condition:
    statement
else:
    statement

if condition:
    statement
elif condition:
    statement
else:
    statement

operator ที่ใช้ใน condition ==, !=, >, >=, <, <=
'''
temp = input("กรุณาป้อนจำนวนเต็ม =") 
N = int(temp)
if (N % 2) == 0:
    print("เลขคู่")
    
print("ไม่ทำอะไร")

#----------------------------------------------

num = int(input("Enter your number (integer): "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")



