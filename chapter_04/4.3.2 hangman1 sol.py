
#*Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - สุ่มเลือกคำจาก word_list และใส่ในตัวแปรชื่อ chosen_word.
import random
chosen_word = random.choice(word_list)

#TODO-2 - ถามผู้ใช้ให้เดาตัวอักษร 1 ตัว แล้วเก็บในตัวแปรชื่อ guess. และแปลงเป็น lowercase.
guess = input("Guess a letter: ").lower()

#TODO-3 - ตรวจสอบว่าตัวอักษรที่ผู้ใช้เดา อยู่ในอักขระตัวตัวหนึ่งใน chosen_word หรือไม่
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
