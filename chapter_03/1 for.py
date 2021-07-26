'''
ในการทำงานซ้ำๆ เราจะใช้ loop
for <variable> in <sequence>: 

'''

for i in range(10):
   print(i)

'''
range เป็นฟังก์ชันที่มีรูปแบบ range(start, stop, step)

'''
x = range(3, 6)
for n in x:
  print(n)

x = range(3, 20, 2)
for n in x:
  print(n)


#ให้เขียนโปรแกรมแสดงสูตรคูณ 
num = int(input("Enter th number of multiplication = "))

# use for loop to iterate 12 times
for i in range(1, 13):
   print(num,'x',i,'=', num*i)

# โปรแกรมแสดงผลรวมตั้งแต่ 1-n
n = int(input("Enter your number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("Sum from 1 to %d" %n ," = ", sum)


'''
ถ้าจะใช้ range สร้าง list ที่เป็นตัวเลขที่เป็นลำดับสามารถทำได้โดย
list(range(begin,end))
'''
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

#----------------------------------------
DayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = input("Enter the date: ")
for day_x in DayOfWeek:
    if day == day_x:
        print("Found : ", day_x)
        break
    else:
        print("Not found :", day_x)

#----โปรแกรมนี้เป็นโปรแกรมทำอะไร
n = int(input("Enter integer number: "))
Sum = 0
for i in range(2, n + 1):
    if i % 2 != 0:
        continue
    else:
        Sum = Sum + i
print("Sum  = ", Sum)
#------โปรแกรมนี้ทำอะไร
n = int(input("Enter number :"))
for i in range(2, n):
    if n % i == 0:
        print(n,"is not a prime")
        break
else:
    print(n, "is a prime")


#โปรแกรมหาค่าเฉลี่ยของข้อมูลใน list 
lst = [23.5, 12.8, 9.75, 18.7, 32.3, 19.0, 26.4, 10.15]
sum = 0
for i in lst:
    sum = sum + i
    n = len(lst)
result = sum / n
print("Average = %.2f" %result)

'''
ในการวน loop บางครั้งเราต้องการให้ข้ามไป 
จะใช้ pass ดังตัวอย่าง
'''
for letter in 'Python': 
   if letter == 'h':
      pass
      #print ("This is pass block")
   else:
       print ("Current Letter :", letter)


#โปรแกรมที่สร้าง List ที่เป็นยกกำลัง 2
squares = []
for value in range(1,11):
 square = value**2
 squares.append(square)
 print(squares)

# โปรแกรมข้างต้น จะเขียนให้สั้นลงอย่างหรือไม่

'''
squares = [value**2 for value in range(1,11)]
print(squares)
# วิธีการนี้เรียกว่า List Comprehension
squares = [value**2 for value in range(1,11) if value%2==1]
'''

# for สามารถใช้กับ list ได้

numbers = [1, 2, 4, 6, 11, 20]
sq = 0
for val in numbers:
    sq = val * val
    print(sq)

#ให้ใช้ List Comprehensions สร้าง List เลข 1-20
#print เฉพาะตัวที่หารด้วย 3 ลงตัว 

#%%
motorcycles = ['yamaha','honda','suzuki']

for i in motorcycles:
  print ("I have "+i+" motercycle.")
#%%

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you, everyone. That was a great magic show!")

# ข้อควรระวัง คือ indent 

#%%
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# ให้เขียนโปรแกรมหาผลบวกของ 1-20 

# ให้เขียนโปรแกรมแสดงผลบวกของ 1-20 เฉพาะเลขคู่ / คี่




# ให้สร้าง List ที่ประกอบด้วยตัวเลขจำนวน 10 ตัว เช่น
# lst1 = [1,5,6,7,2,8,9,10,100,12]
# ให้เขียนโปรแกรมเพื่อพิมพ์ค่าที่มากที่สุดใน List (ห้ามใช้ function)

# ให้เขียนโปรแกรมเพื่อพิมพ์ค่าที่น้อยที่สุดใน List (ห้ามใช้ function)

# 

# 



#
cars = ['audi', 'bmw', 'subaru', 'toyota']

#
for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())


'''
ในการทำงานบางอย่าง ต้องใช้ loop มากกว่า 1 loop
'''
stds_height = [[125, 130, 142, 135, 145],
            [132, 137, 155, 154, 158],
            [150, 154, 155, 153, 160],
            [152, 153, 156, 151, 160],
            [153, 154, 156, 157, 162],
            [155, 156, 154, 160, 162]]

Total_average = 0
Total_year = 0
Average_each_year = []

for i in stds_height:
    sum = 0
    for j in i:
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