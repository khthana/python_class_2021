# ---------------------------
# การดำเนินเกี่ยวกับไฟล์
# ประกอบด้วย 3 ขั้นตอนหลัก คือ 1) เปิดไฟล์ 2) ดำเนินการ 3) ปิดไฟล์

# 1) เปิดไฟล์
# file object = open(file_name [, access_mode][, buffering])
# r     = เปิดไฟล์ที่มีอยู่แล้วเพื่ออ่านเพียงอย่างเดียว
# r+    = เปิดไฟล์เพื่ออ่านและเขียน โดยที่ข้อมูลเก่ายังคงอยู่
# w     = เปิดไฟล์เพื่อเขียน ถ้ามีไฟล์อยู่แล้ว ข้อมูลในไฟล์เดิมจะถูกเขียนทับ ถ้าไม่มีไฟล์อยู่ จะสร้างไฟล์ขึ้นใหม่
# w+    = เปิดไฟล์เพื่ออ่านและเขียน ถ้ามีไฟล์อยู่แล้ว ข้อมูลในไฟล์เดิมจะถูกเขียนทับ ถ้าไม่มีไฟล์อยู่ จะสร้างไฟล์ขึ้นใหม่
# a     = เปิดไฟล์เพื่อเขียนข้อมูลต่อท้าย ในกรณีที่มีไฟล์อยู่แล้วจะเขียนข้อมูลต่อ ถ้าไม่มีไฟล์อยู่ จะสร้างไฟล์ขึ้นใหม่

# f = open("MyFile.txt", "w")

# 2) ดำเนินการ

# f.read(n)        อ่านไฟล์ทั้งไฟล์ โดย n คือ จำนวนตัวอักษรที่ต้องการอ่าน ไม่กำหนดอ่านทั้งไฟล์
# f.readline(n)    อ่านไฟล์ครัังละ 1 บรรทัด คือ อ่านจน '\n' : ไม่กำหนด n อ่าน 1 บรรทัด
# f.readlines(n)   อ่านไฟล์หลายบรรทัด ส่งกลับเป็น list ของแต่ละบรรทัด

# f.write()        เขียนไฟล์ 1 บรรทัด
# f.write(str1)
# f.writelines()   เขียนไฟล์หลายบรรทัด
# f.writelines(L) for L = [str1, str2, str3]

# f.seek(n)        เลื่อน file pointer ไปที่ n

# 3) ปิดไฟล์
# fileObject.close()

# f.close()

# ตัวอย่าง
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n คือ EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print('\n')

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print('\n')

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print('\n')

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print('\n')
file1.close()

# relative / absolute path
