"""
* Tuple เป็นโครงสร้างข้อมูลที่เก็บข้อมูลหลายตัว คล้ายกับ List
* การสร้าง Tuple จะใช้เครื่องหมาย ()
* ความแตกต่างกับ List คือ Tuple จะใช้เก็บข้อมูลที่มีค่าคงที่ และไม่มีการเปลี่ยนแปลง
* ดังนั้นจะแก้ไข Tuple ไม่ได้
"""

#%%
tup0 = ()
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = (19, 12.5, 'Python',"HELLO")     #| จะมีวงเล็บ
tup4 = 'a','b','c'                      #| หรือไม่มีวงเล็บก็ได้
tup5 = (tup1, tup2, tup3)
tup6 = tup1 + tup2
tup7 = tup1 * 5
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)
print(tup6)
print(tup7)
print(tup1[0])
print(len(tup3))
print(3 in tup1)        # ตรวจสอบการมีข้อมูล

#%%
tup10 = (30)
tup20 = (30,)
print("Tuple 10 :",tup10)
print("Tuple 20 :",tup20)

#%%
tup1, tup2 = (1, 2)
print(tup1)
print(tup2)
tup1, tup2 = (1, 2), (3, 4);

#* จากข้อมูลในหน้าเว็บนี้ 
#* http://www.berdee.com/dooduangberdee.html
#* จงเขียนโปรแกรมตรวจสอบเบอร์มงคล
#* โดยรับหมายเลขโทรศัพท์เข้ามา
#* ให้เขียนเป็น function ให้เหมาะสม





# %%
