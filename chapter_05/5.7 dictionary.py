#---------------------------------------------------
#* ในขณะที่ list เป็นโครงสร้างข้อมูลที่อ้างอิงโดย Index
#* เป็นโครงสร้างข้อมูล ในลักษณะของการจับคู่ ซึ่งอ้างอิงโดย Key
#* การใช้งานจะเป็นรูปแบบ {key : value, key : value}
#---------------------------------------------------

scores = {'james': 1828, 'thomas': 3628, 'danny': 9310}

#---------------------------------------------------
#* การเพิ่มข้อมูล จะระบุด้วย key
#---------------------------------------------------
scores['bobby'] = 4401

#---------------------------------------------------
#* การแก้ไขข้อมูล ก็ใช้ key เป็นตัวอ้างอิงเช่นกัน
#---------------------------------------------------
scores['james'] = scores['james'] + 1000

#---------------------------------------------------
#* การแสดงผล ใช้ key เป็นตัวอ้างอิง
#---------------------------------------------------
print('james =>', scores['james'])
print('thomas =>', scores['thomas'])

#---------------------------------------------------
#* กรณีที่ Value มีหลายจำนวน อาจใช้ Value เป็น List ได้
#---------------------------------------------------
std_info = {62001: ["Somsri Medee", 23, "4 Jun 2000", "somsri@gmail.com","066-12345678"]}

print(std_info)
print(std_info[62001])
print(std_info[62001][2])

#---------------------------------------------------
#* สามารถอ้างถึงแต่ละส่วนได้ ทั้ง keys และ value 
#---------------------------------------------------
print(std_info[62001])
print(std_info.keys())
print(std_info.values())

#---------------------------------------------------
#* Dictionary สามารถใช้กับ for loop ได้ 
#---------------------------------------------------
countries = {'de': 'Germany', 'ua': 'Ukraine',
             'th': 'Thailand', 'nl': 'Netherlands'}

for i in countries:
    print(i)

for k, v in countries.items():
    print(k, v)

# iterate through keys
print('Key:', end = ' ')
for k in countries.keys():
    print(k, end = ' ')

# iterate through values
print('\nValue:', end = ' ')
for v in countries.values():
    print(v, end = ' ')

### Example--------------------------------------

num = int(input("Enter the number of students:"))
dic = {}
while num > 0:
    idx = input("Enter your ID:")
    name = input("Enter your name:")
    age = input("Enter your age:")
    dic[idx] = [name, age]
    num = num - 1
#print all student members
print(dic)
#print each student member
for data in dic:
    print(dic[data])

#------------------------------------------------------
dic = {"10110":"เขตคลองเตย", "50000":"อำเภอเมืองเชียงใหม่", "21000":"อำเภอเมืองระยอง", "40000":"อำเภอเมืองขอนแก่น", "83000":"อำเภอเมืองภูเก็ต"}
amphor = input("Enter your the code of amphor that would like to find :")
while amphor != "exit":
    if dic[amphor]:
        print("Name of this code is ", dic[amphor])
    else:
        print("This code is not in the database")
    amphor = input("Enter your the code of amphor that would like to find :")
print("Good bye...")

