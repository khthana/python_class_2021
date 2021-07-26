"""
* String มี Function ให้ใช้มากมาย 
* วิธีการใช้ Function ของ String จะใช้ .fn หลังตัวแปร
"""
# %%
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#* การตัดช่องว่าง หน้า-หลัง
# %%
favorite_language = 'python '
print(favorite_language+':')
print(favorite_language.rstrip()+':')
# %%
favorite_language = ' python '
print(':'+favorite_language)
print(':'+favorite_language.lstrip())

#* เราสามารถใช้ String Function ต่อกันได้ด้วย 
s = " Python 3.6 "
s = s.strip().upper()
print(s)

"""
* การแปลงค่าระหว่างชนิด
* การแปลงค่าจาก str เป็น int
* int(number, base=base)
## int("10")
## 10
## int("10",base=2)
## 2

* การแปลงจาก int เป็น str
* str(num)
## str(123)
## '123'

"""

"""
* Format String
## name = 'Bob
## 'Hello, %s' % name
## "Hello, Bob"
"""

num = 3
print ('Hello, %s' % num)
print ('Hello, %s %s' % (num, num))
print ('Hello, %10s %10s' % (num, num))

