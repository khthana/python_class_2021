"""
* String สามารถแยกออกเป็นตัวอักษรได้ โดยเริ่มจาก 0
* String slicing
str1 = 'Hello World!'
str1[6]: W
str1[1:5]:ello
"""
str1 = 'Hello World!'
print (str1[6])
print (str1[1:5])

"""
*นอกจากนั้นยังอ้างจากท้ายได้ด้วย 
word = 'Python'
word[-1] = 'n'
word[-2] = 'o'
word[5] = ??
"""

s1 = "Python Programming"
print(s1[7:])
print(s1[-11:])


"""
*และอ้างแบบกระโดดได้ด้วย 
s = '0123456789'
s[2:8:2] = '246'
"""

"""
s[:5] = '01234'
s[4:] = '456789'
s[::3] = '0369'
s[::-2] = '97531'
"""

#* Ex.จงหา s[-1:2:-2] จากรหัสนักศึกษาของตัวเอง 

#* operator in กับ string
#* 'k' in "kmitl"


#*กรณีทีข้อมูลเป็นชุดที่คั่นด้วยตัวอักษร สามารถแยกด้วยฟังก์ชัน split เช่น
#*โดยผลลัพธ์จะอยู่ใน List 

text= 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splits at ':'
print(grocery.split(':'))

#*การรวมชุด string ที่คั่นด้วย , จะใช้ join 

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))
