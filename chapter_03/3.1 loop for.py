#-------------------------------------------
#* ในการทำงานซ้ำๆ เราจะใช้ loop
#* for <variable> in <sequence>:
#-------------------------------------------

#-------------------------------------------
#* ตัวอย่างการใช้ loop ในการเข้าถึง list 
#-------------------------------------------
flowers = ['calla', 'lily', 'jasmine', 'forget me not', 'sunflower', 'ivy', 'gypso']
for f in flowers:
    print (f)

#-------------------------------------------
#* อีกวิธีหนึ่งสามารถอ้างได้ทั้ง index และ ค่าใน list 
#-------------------------------------------

for i, e in enumerate(flowers):
    print("{}. {}".format(i+1, e))

#-------------------------------------------
#* ตัวอย่างการใช้ loop เพื่อค้นหาข้อมูลใน list 
#-------------------------------------------
DayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = input("Enter the date: ")
for day_x in DayOfWeek:
    if day == day_x:
        print("Found : ", day_x)
        break
    else:
        print("Not found :", day_x)

#| Ex.3.1 จาก List ที่กำหนดให้ เป็นความสูงของนักเรียนในชั้น ให้หาค่าเฉลี่ยของความสูง
#| แสดงทศนิยม 2 ตำแหน่ง (ห้ามใช้ฟังก์ชัน)

height = [170, 165, 175, 172, 163, 169, 172, 155,162]


#| Ex.3.2 ให้แก้ไขโปรแกรมโดยรับจากคีย์บอร์ด ในรูปแบบ 170, 165...

#sum = 0
#for i in lst:
    #sum = sum + i
    #n = len(lst)
#result = sum / n
#print("Average = %.2f" %result)

#| Ex.3.2 ให้เขียนโปรแกรมรับคะแนนจากคีย์บอร์ด คั่นด้วย , 
#|        จากนั้นหาคะแนนที่มากที่สุด และ น้อยที่สุด (ห้ามใช้ฟังก์ชัน)


#-------------------------------------------
#* การใช้ for กับ list อาจทำกับบางส่วนของ list 
#* โดยใช้ slicing ก็ได้
#-------------------------------------------
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#-------------------------------------------
#* loop for กับฟังก์ชัน range
#* เป็นรูปแบบที่อาจจะใช้มากที่สุดของ loop 
#-------------------------------------------

for i in range(10):
       print(i)

#-------------------------------------------
#* range เป็นฟังก์ชันที่มีรูปแบบ range(start, stop, step)
#* • for k in range(10) : k = 0, 1, 2, ..., 9
#* • for k in range(2,10) : k = 2, 3, 4, ..., 9
#* • for k in range(2,10,2) : k = 2, 4, 6, 8
#* • for k in range(10,1,-2) : k = 10, 8, 6, 4, 2
#* • for k in range(11,11) : ไม่ทำ เพราะ step เป็นบวก และ start >= stop
#* • for k in range(9,10,-1) : ไม่ทำ เพราะ step ติดลบ และ start <= stop
#! range จะไม่รวมตัวสุดท้าย for k in range(1,5) k = 1,2,3,4
#-------------------------------------------
x = range(3, 6)
for n in x:
    print(n)

x = range(3, 20, 2)
for n in x:
    print(n)

### ตัวอย่าง เขียนโปรแกรมแสดงสูตรคูณ
### โปรแกรมนี้มี 1 input คือ แม่สูตรคูณ
### Output แสดงแต่ละบรรทัด 4 x   1 = 4

num = int(input("Enter th number of multiplication = "))
# use for loop to iterate 12 times
for i in range(1, 13):
    print(f'{num} x {i:2} = {num*i:3}')

### ตัวอย่าง เขียนโปรแกรมแสดง ascii table
for i in range(65, 128):
        print(f"{i:3} {i:#08b} {i:04o} {i:#x} {i:X} {i:c}")

#| Ex.3.3 ให้เขียนโปรแกรมแสดงตารางเทียบอุณหภูมิระหว่าง C กับ F
#|        F= C/5*9+32

#-------------------------------------------

#| Ex.3.4 โปรแกรมแสดงผลรวมตั้งแต่ 1-n
n = int(input("Enter your number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum from 1 to %d" %n ," = ", sum)

#-------------------------------------------

#| Ex.3.5 โปรแกรมแสดงผลรวมตั้งแต่ 1-n เฉพาะเลขคี่

### ตัวอย่างให้เขียนโปรแกรมเพื่อพิมพ์ค่าที่มากที่สุดใน List

#-------------------------------------------

#| Ex 3.6 ให้เขียนโปรแกรมคำนวณ Factorial
#|        Factorial 5 = 5x4x3x2x1


#-------------------------------------------

#| Ex 3.7 เกมที่คนที่นับถึงตัวที่หารด้วย 3 หรือ 5 แทนที่จะบอกเป็นตัวเลข
#| ให้พูดเป็นคำอื่น ให้เขียนโปรแกรม ที่แสดงตัวเลขตั้งแต่ 1-100 แต่เมื่อถึง
#| ตัวที่หารด้วย 3 ลงตัวให้แสดงเป็น Fizz เมื่อเจอตัวที่หารด้วย 5 ลงตัว ให้แสดง Buzz
#| ถ้าหารทั้ง 3 และ 5 ลงตัวให้แสดง Fizz Buzz 

#-------------------------------------------
#* โปรแกรมหา day of week เขียนได้อีกแบบ โดยใช้ range
#-------------------------------------------
DayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = input("Enter the date: ")
for day_x in range(len(DayOfWeek)):
    if day == DayOfWeek[day_x]:
        print("Found : ", DayOfWeek[day_x])
        break
    else:
        print("Not found :", DayOfWeek[day_x])

#-------------------------------------------

#| การอ่านโปรแกรมก็เป็นวิธีการพัฒนาทักษะวิธีหนึ่ง 
#| Ex 3.7 -- โปรแกรมนี้เป็นโปรแกรมทำอะไร ---

n = int(input("Enter integer number: "))
Sum = 0
for i in range(2, n + 1):
    if i % 2 != 0:
        continue
    else:
        Sum = Sum + i
print("Sum  = ", Sum)

#-------------------------------------------

#| Ex 3.8 ------โปรแกรมนี้ทำอะไร ------------
n = int(input("Enter number :"))
for i in range(2, n):
    if n % i == 0:
        print(n,"is not a prime")
        break
else:
    print(n, "is a prime")

#---------------------------------------------------
#* ถ้าจะใช้ range สร้าง list ที่เป็นตัวเลขที่เป็นลำดับสามารถทำได้โดย
#* list(range(begin,end))
#---------------------------------------------------
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

#* ตัวอักษรทุกตัวจะมีรหัสประจำอยู่เรียกว่า ASCII
#* เราสามารถหาค่า ASCII ได้ โดยใช้ ord
#* ascii = ord('a')

#| Ex.3.9 จงเขียนโปรแกรมแสดง ascii ตั้งแต่ 1-127 