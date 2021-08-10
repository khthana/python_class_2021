#-------------------------------------------
#* ในการใช้งานบางงาน เราอาจใช้วิธี "นำเข้า" โปรแกรม
#* ที่ผู้อื่น หรือ ตัวเองเขียนที่อยู่ในไฟล์อื่น เรียกว่า "โมดูล"
#
#* ใช้คำสั่ง import module
#
#* โมดูลแรกที่จะลองใช้ คือ random ซึ่งใช้สุ่มเลข

import random 

random_side = random.randint(0,1)
# คำสั่ง randint(start,stop) จะสุ่มจำนวนเต็มตั้งแต่ start - stop
if random_side == 1:
    print("Heads")
else:
    print("Tails")

#| Ex.2.9 จงเขียนโปรแกรมเป่ายิงฉุบ 
#| โดยให้รับข้อมูลจาก User จำนวน 1 ตัวเป็น [R]ock, [P]aper, [S]cissors
#| จากนั้นให้สุ่มเลือกคอมพิวเตอร์ 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#-------------------------------------------------------------------------
#*  List เป็นโครงสร้างที่สามารถเก็บข้อมูลได้หลายตัวต่อกัน สามารถเก็บข้อมูลต่างชนิดกันได้ P94
#*  เนื่องจากบางครั้งเราจะเก็บข้อมูลที่เป็นชุด เช่น ข้อมูลจังหวัด ในกรณีนี้เราจะใช้ List หรือ Tuple
#*  การสร้าง List จะใช้เครื่องหมาย [] เช่น
#
#*  lst = [1, 2, 3, 4, 'Foo', 5, 'Bar']
#*  weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#*  list0 = []
#*  list2 = [1, 2, 3, 4, 5 ]
#*  list3 = ["a", "b", "c", "d"]
#*  list4 = list('abcde') => ['a', 'b', 'c', 'd', 'e']
#
#*  การอ้างถึงข้อมูลใน list จะใช้ตัวเลข โดยเริ่มจาก 0 เช่น list3[1] คือ "b"
#*  การอ้างถึงคล้ายกับ string ใช้วิธีเดียวกันได้ทั้งหมด
#-------------------------------------------------------------------------

std_info = [62001, "Somsri Medee", 23, "4 Jun 2000", "somsri@gmail.com","066-12345678"]
print(std_info)

list1 = ['physics', 'chemistry', 'calculus', 'biology'];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]:", list1[0])
print ("list1[-1]:", list1[-1])
print ("list2[3]:", list2[3])
print ("list2[-4]:", list2[-4])
print ("list2[1:5]:", list2[1:5])
print ("list2[::2]:", list2[::2])
print ("list2[2::2]:", list2[2::2])
print ("list2[2:7:2]:", list2[2:7:2])
print ("list2[:7]:", list2[:7])
print ("list2[4:]:", list2[4:])

#| Ex.2.10 ให้สร้าง List ชื่อเพื่อนจำนวน 3 คน 
#| print hello ชื่อเพื่อนให้ครบทุกคน

#---------------------------------------------------------------
#* การเพิ่มข้อมูลใน List สามารถหลายวิธี เช่น ใช้ + หรือ append หรือ extend
#---------------------------------------------------------------

flowers = ['Rose','Lily','Tulip','Carnation','Poppy','Sunflower']
print(flowers)

#---------------------------------------------------------------
#* ดูโปรแกรมต่อไปนี้ แล้วบอกความแตกต่างระหว่าง extend กับ append และ +
#---------------------------------------------------------------
flowers.append(['Iris'])
print(flowers)
flowers.extend(['Violet'])
print(flowers)
flowers.append('Jasmine')
print(flowers)
flowers.extend(['Lavender'])
print(flowers)
flowers.append('Jasmine')
print(flowers)

flowers += ['Magnolia']
print(flowers)
flowers += 'Rosemary'
print(flowers)


#| Ex.2.11 ให้เขียนโปรแกรมรับชื่อเพื่อนจาก Keyboard จำนวน n คน ใน 1 บรรทัด
#|         เพิ่มชื่อเพื่อนใน list และสุ่มเลือกเพื่อนมา 1 คนและแสดงผล
#|         การแยกแต่ละตัวของ string จะใช้ split เช่น 
#|         name_list = name.split(", ")


#---------------------------------------------------------------
#* การแก้ไขข้อมูลตัวใดตัวหนึ่งใน list ทำได้โดยระบุตำแหน่งและกำหนดข้อมูลใหม่
#---------------------------------------------------------------

list1 = ['physics', 'chemistry', 'calculus', 'biology'];
print ("Old value available at index 2 : ",list1[2])
list1[2] = 'programming';
print ("New value available at index 2 : ",list1[2])
print(list1)

#---------------------------------------------------------------
#* การแทรกข้อมูลใน List จะใช้ insert โดยระบุตำแหน่งที่ insert
#---------------------------------------------------------------

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

#---------------------------------------------------------------
#* การลบข้อมูลใน List ทำได้หลายวิธี
#*      clear เป็นการลบ list ทั้งหมด
#*      remove เป็นการลบโดยอ้างถึงค่า
#*      del เป็นการลบโดยอ้างถึงตำแหน่ง
#*      pop 
#---------------------------------------------------------------

motorcycles = ['honda','yamaha','suzuki','ducati']

print(motorcycles)
del motorcycles[2]
print(motorcycles)
motorcycles.pop(0)
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.clear()
print(motorcycles)

#---------------------------------------------------------------
#* เราสามารถตรวจสอบว่า มีข้อมูล หรือ ไม่มีข้อมูลใน list หรือไม่ โดยใช้ in
#---------------------------------------------------------------

motorcycles = ['honda','yamaha','suzuki','ducati']
print ('ducati' in motorcycles)
print ('toyata' not in motorcycles)


#---------------------------------------------------------------
#* list สามารถ เปรียบเทียบได้ด้วย เช่น
#* โดยการเปรียบเทียบจะเปรียบเทียบเรียงตามลำดับ 
#* ดังนั้น [1,2] จะไม่เท่ากับ [2,1]
#---------------------------------------------------------------
lst1 = [1,2,3,4,5]
lst2 = [9,8,7,6,5]
lst3 = [9,8,7,6,5]
lst4 = [8,7]
print("lst1 < lst2 :",lst1 < lst2)
print("lst1 > lst2 :",lst1 > lst2)
print("lst2 >= lst1 :",lst2 >= lst1)
print("lst2 == lst3 :",lst2 == lst3)

#---------------------------------------------------------------
#* กรณีที่ต้องการสร้างข้อมูลที่มีลำดับที่แน่นอน เราสามารถใช้ range(start, stop, step)
#* start = เริ่ม, stop = สิ้นสุด (ไม่รวม stop), step = กระโดดครั้งละ
#---------------------------------------------------------------
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)

numbers = list(range(1, 6))
print(numbers)


