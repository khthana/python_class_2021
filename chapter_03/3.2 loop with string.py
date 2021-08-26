#-------------------------------------------
#* เนื่องจาก string มีลักษณะคล้ายกับ list
#* ดังนั้นจึงมีการใช้ loop กับ string ได้หลายรูปแบบ
#-------------------------------------------

#-------------------------------------------
#* การวน Loop ใน String
#* ต้องการนับว่าสตริง s มีสระกี่ตัว
#-------------------------------------------
s = "Nobody can predict the future, only a firm grasp on the present."
c = 0
for e in s :
    if e in['a','e','i','o','u']:
        c += 1
print(f"String has vowel {c} charecters.")

#-------------------------------------------

#| Ex 3.10 จงเขียนโปรแกรมที่นับว่าสตริง s มีตัวที่ติดกันเป็นตัวเลขทั้งคู่อยู่กี่คู่

for k in range(len(s)-1) : # ต้องการตัวติดกัน จึงวนถึงตัวรองสุดท้าย
    if '0' <= s[k] <= '9' and '0' <= s[k+1] <= '9' :
        c += 1

#-------------------------------------------

### ตัวอย่าง ต้องการหาว่าใน string มีอักขระพิเศษกี่ตัว

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter your string = ")
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

#| Ex 3.11 จงเขียนโปรแกรมรับค่าทะเบียนรถ และ หาค่า sum ของตัวเลข

#| Ex 3.12 เขียนโปรแกรมคำนวณหลักสุดท้ายของบัตรประชาชน

citizen_id = input("Enter citizen ID : ")


#-------------------------------------------
#* ในการวน loop บางครั้งเราต้องการให้ข้ามไป
#* จะใช้ pass ดังตัวอย่าง
#-------------------------------------------

for letter in 'Python':
    if letter == 'h':
        pass
        #print ("This is pass block")
    else:
        print ("Current Letter :", letter)

#-------------------------------------------
#* การออกจาก Loop จะใช้ break
#-------------------------------------------

for i in range(5):
    for j in range(6):
        print(f'j={j}')
        if (j==4):      # condition 1
            break       # break นี้ออกจาก for j
    print(f'i={i}')
    if (i==2) :         # condition 2
        break           # break นี้ออกจาก for i

### ตัวอย่าง โปรแกรมที่สร้าง List ที่เป็นตัวเลขยกกำลัง 2 

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)

### โปรแกรมข้างต้น จะเขียนให้สั้นลงอย่างหรือไม่

squares = [value**2 for value in range(1,11)]
print(squares)

#-------------------------------------------
#* วิธีการนี้เรียกว่า List Comprehension
#* โครงสร้างจะมี 2 ส่วน คือ หน้า for กับหลัง for
#* ส่วนหลัง for จะเป็นคำสั่ง for ตามปกติ
#* ส่วนหน้า for จะเป็นคำสั่งที่ execute ตาม loop ได้คำสั่งเดียวหรือ fn
#* ผลลัพธ์ที่ได้จะอยู่ใน list
#-------------------------------------------

#-------------------------------------------
#* จากตัวอย่างนี้ จะเห็นว่าใน for ยังสามารถใส่เงื่อนไขของ if ได้อีกด้วย
#-------------------------------------------

squares = [value**2 for value in range(1,11) if value%2==1]

#-------------------------------------------

#| Ex. 3.13 ให้ใช้ List Comprehensions สร้าง List เลข 1-20
#|          แล้ว print เฉพาะตัวที่หารด้วย 3 ลงตัว


#-------------------------------------------
#* ในการทำงานบางอย่าง ต้องใช้ loop มากกว่า 1 loop
#-------------------------------------------

### ตัวอย่าง กำหนดให้ มีข้อมูลความสูงของนักเรียน 6 ชั้นปี
### ให้หาความสูงเฉลี่ยของนักเรียนในแต่ละชั้นปี 
### และความสูงเฉลี่ยของนักเรียนทั้งหมด

stds_height =  [[125, 130, 142, 135, 145],   # year 1
                [132, 137, 155, 154, 158],
                [150, 154, 155, 153, 160],
                [152, 153, 156, 151, 160],
                [153, 154, 156, 157, 162],
                [155, 156, 154, 160, 162]]

Total_average = 0
Total_year = 0
Average_each_year = []

for i in stds_height:   # list of each year 
    sum = 0
    for j in i:         # each student [125, 130, 142, 135, 145]
        sum = sum + j
    average = sum / len(i)
    Average_each_year.append(average)
    Total_year = Total_year + 1
    Total_average = Total_average + average

print("Total number of years =",Total_year)
for i in range(0, Total_year):
    print("Student height of year",i+1, "=", Average_each_year[i])
print("Overall of student height = %.2f" %(Total_average/Total_year))

#-------------------------------------------
#* โปรแกรมบวก Matrix
#-------------------------------------------

a = [[4, 1, 7],
     [2, 4, 8],
     [3, 7, 1]]

b = [[6, 8, 1],
     [9, 7, 5],
     [2, 4, 3]]

c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for r in c:
    print(r)