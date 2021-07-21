
#*การกำหนดค่าให้ตัวแปร
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

#*string มีอักขระพิเศษ ขึ้นต้นด้วย \
# %% 
print("\tPython")
print("Hello\nPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#*การตัดช่องว่าง หน้า-หลัง
# %%
favorite_language = 'python '
print(favorite_language+':')
print(favorite_language.rstrip()+':')
# %%
favorite_language = ' python '
print(':'+favorite_language)
print(':'+favorite_language.lstrip())

#! Error ที่อาจเกิดขึ้นของ string
# %%
message = 'One of Python's strengths is its diverse community.'
print(message)

#%%
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)

