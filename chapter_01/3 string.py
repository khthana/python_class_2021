
#* String เป็นข้อความ จะใช้ "" หรือ '' ครอบ
# %%
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)


#*string สามารถเอามาต่อกันได้โดยเครื่องหมาย +
# %% 

message = "Hello Python world!"
message2 = 'Welcome to python!'
print (message+'\n'+message2)

#%%
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s3)
print("Hello" + "World")

#*string สามารถทำซ้ำโดยการ *
# %% 

message = "KMITL"
print(message*5)

# %%
message = 'KMITL'
print ('welcome to '+message)

#* ถ้า string มีอักขระพิเศษ จะขึ้นต้นด้วย \
#* ถ้าต้องการแสดง " ให้ใช้ \" หรือ ' ให้ใช้ \'
# %% 
print("\tPython")
print("Hello\nPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#| Ex. ให้เขียนคำสั่งที่พิมพ์ I'm computer engineer. เป็น 3 บรรทัด
#|     ในคำสั่งเดียว

#* กรณีข้อความมีตัวอักษร ' หรือ "
message = 'One of Python's strengths is its diverse community.'
print(message)
print("I'm Python.")
print('''I'm "Python".''')
print("""I'm "Python".""")


#%% String กับ ตัวเลข

age = 23
message = "Happy " + age + "rd Birthday!"
print(message)

#* การหาความยาว String จะใช้ len
len("Hello")

#* การ Print 
#* เราสามารถ print string แบบอื่นๆ

# %%
print("Hello", "how are you?", sep="---") 

# %%
a = 5
print("a = ", a, sep='00000', end='\n\n\n')
print("a = ", a, sep='0', end='\n')

str1 = "Hello"
str2 = "python"
print(str1, end='')
print(str2)

#|Ex. print คำว่า I'm computer engineer. โดยแยกเป็น 3 บรรทัด 
# %%
