'''
เป็นโครงสร้างข้อมูล ในลักษณะของการจับคู่ 
ระหว่างข้อมูลทีเป็น Keys กับ value
การใช้งานจะเป็นรูปแบบ {key : value, key : value}
เช่น
scores = {'james': 1828, 'thomas': 3628, 'danny': 9310}

การเพิ่มข้อมูล จะใช้ตามตัวอย่าง
scores['bobby'] = 4401

การแก้ไขข้อมูล เช่น
scores['james'] = scores['james'] + 1000

การแสดงผล ใช้
print('james =>', scores['james'])
print('thomas =>', scores['thomas'])

'''

std_info = {62001: ["Somsri Medee", 23, "4 Jun 2000", "somsri@gmail.com","066-12345678"]}
print(std_info)

print(std_info[62001])

print(std_info.keys())

'''
Dictionary สามารถใช้กับ for loop ได้ 
'''
countries = {'de': 'Germany', 'ua': 'Ukraine',
             'th': 'Thailand', 'nl': 'Netherlands'}

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

#---------------------------------------------------
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
print("Good bye...")

