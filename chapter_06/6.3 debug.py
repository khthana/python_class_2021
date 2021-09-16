#-----------------------------------------------------------
#* Tips การ debug
#*      1. ระบุปัญหาให้ชัดเจน
#*      2. ทำซ้ำปัญหาได้
#*      3. มองในมุมของคอมพิวเตอร์
#*      4. แก้ไขข้อผิดพลาด
#*      5. Print is Your Friend
#*      6. ฝึกใช้ debugger
#*      7. พักผ่อน
#*      8. ถามเพื่อน
#*      9. รันโค้ดระหว่างเขียนบ่อยๆ เพื่อตรวจสอบความผิดพลาดทีละส่วน
#*      10. stack overflow 

############DEBUGGING#####################
### ให้ยกเลิก comment ทีละส่วนและ Run 

# # ระบุปัญหาให้ชัดเจน
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # ทำซ้ำปัญหาได้
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # มองในมุมของคอมพิวเตอร์
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # แก้ไขข้อผิดพลาด
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])