#%%
"""
* ตัวแปรมี 4 ชนิด คือ string, int, float, boolean 
"""
message = "One of Python's strengths is its diverse community."  #! String

print(message)

# %%
a = "hello"     #! String
print(a)
print(type(a))

a = 10          #! integer
print(a)
print(type(a))

a = 10.0        #! Float
print(a)
print(type(a))

a = True        #! boolean
print(a)
print(type(a))

#*  การยกเลิกตัวแปร
s1 = "Python Programming"
print(s1)
del s1
print(s1)

"""
!หลักการตั้งชื่อตัวแปร
 Camel Case เป็นการตั้งชื่อโดยกำหนดให้คำแรกเป็นตัวอักษรตัวเล็ก
 ทั้งหมด แต่ไม่ได้ใช้อักษรย่อ การตั้งชื่อแบบ Camel Case 
 จะเป็นคำต่อกันทั้งหมด ซึ่งตัวอักษรตัวแรกของคำที่ 2 ขึ้นไป 
 จะเป็นตัวใหญ่

? productPrice
? summaryResult

Snake Case แทนที่จะแบ่งคำด้วยตัวอักษรตัวเล็กตัวใหญ่ 
(case sensitive) การตั้งชื่อแบบนี้จะใช้ _ (Underscore) แทน

? product_price
? summary_result

!และควรตั้งชื่อให้ยาวพอที่จะสื่อความหมาย
"""

#* Ex.1 ให้ตั้งตัวแปร 3 ตัว เป็นชนิด Int, Float และ String 

