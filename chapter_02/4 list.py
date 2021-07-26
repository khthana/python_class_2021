'''
List เป็นโครงสร้างที่สามารถเก็บข้อมูลได้หลายตัวต่อกัน สามารถเก็บข้อมูลต่างชนิดกันได้ P94
การสร้าง List จะใช้เครื่องหมาย [] เช่น

lst = [1, 2, 3, 4, 'Foo', 5, 'Bar']
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
list0 = []
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

การอ้างถึงข้อมูลใน list จะใช้ตัวเลข โดยเริ่มจาก 0 เช่น list3[1] คือ "b"
การอ้างถึงคล้ายกับ string ใช้วิธีเดียวกันได้ทั้งหมด 

'''
#%%
std_info = [62001, "Somsri Medee", 23, "4 Jun 2000", "somsri@gmail.com","066-12345678"]
print(std_info)

#%%
list1 = ['physics', 'chemistry', 1997, 2000];
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

# ให้สร้าง List ชื่อเพื่อนจำนวน 3 คน 
# print hello ชื่อเพื่อนให้ครบทุกคน


'''
การแก้ไขข้อมูลตัวใดตัวหนึ่งใน list 
'''
list = ['physics', 'chemistry', 1997, 2000];
print ("Old value available at index 2 : ",list[2])
list[2] = 2001;
print ("New value available at index 2 : ",list[2])
print(list)
'''
การเพิ่มข้อมูลใน List 
'''
std_info = [62001, "Somsri Medee", 23, "4 Jun 2000", "somsri@gmail.com","066-12345678"]
print(std_info)
std_info.append(45000)
print(std_info)

'''
การลบข้อมูลใน list 
'''
std_info = [62001, "Somsri Medee", 23, "4 Jun 2000", "somsri@gmail.com","066-12345678"]
print(std_info)
del std_info[2]
print(std_info)
print(std_info[1])

#%%

'''
การแทรกข้อมูลใน List
'''

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

'''
การลบแบบระบุชื่อ
'''
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#%%
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#%%
# ให้ทดลองทำ List ชื่อเพื่อน ที่จะมา Party 
# print ข้อความและชื่อ
# ให้ เพิ่มชื่อ ลบชื่อ โดยใช้ insert, append และ remove






'''
การบวก List 
'''
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print (len(lst1))

lst1 = lst1+lst2
print (len(lst1))
print (lst1)

'''
เราสามารถตรวจสอบว่า มีข้อมูล หรือ ไม่มีข้อมูลใน list หรือไม่
3 in lst1
3 not in lst1
'''
lst1 = [1, 2, 3]
print(3 in lst1)
print(3 not in lst1)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

'''
list สามารถ เปรียบเทียบได้ด้วย เช่น 
lst1 = [1,2,3,4,5]
lst2 = [9,8,7,6,5]
lst3 = [9,8,7,6,5]
lst4 = [8,7]
print("lst1 < lst2 :",lst1 < lst2)
print("lst1 > lst2 :",lst1 > lst2)
print("lst2 >= lst1 :",lst2 >= lst1)
print("lst2 == lst3 :",lst2 == lst3)

โดยการเปรียบเทียบจะเปรียบเทียบเรียงตามลำดับ 
ดังนั้น [1,2] จะไม่เท่ากับ [2,1]
'''
print ([3,2,3]<[2,1,1])

#range เป็นฟังก์ชันที่มีรูปแบบ range(start, stop, step) 
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)
# %%
numbers = list(range(1, 6))
print(numbers)


