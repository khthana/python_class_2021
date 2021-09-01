
#| Ex 4.7 Hangman Step 2 ให้ทำงานใน TODO ให้ครบทั้ง 3 ข้อ

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - สร้าง List ว่าง และตั้งชื่อว่า display.
#* ให้เพิ่ม '_' ใน list display เท่ากับจำนวนตัวอักษรใน chosen_word
#* เช่น หาก chosen_word เป็น "apple", display จะเป็น ["_", "_", "_", "_", "_"]

guess = input("Guess a letter: ").lower()

#TODO-2: - วน Loop ไปแต่ละตำแหน่งใน chosen_word
#* ถ้าตัวอักษรในตำแหน่งนั้นตรงกับ 'guess' ให้เปลี่ยนตัวอักษรใน display เป็น guess ในตำแหน่งเดียวกัน
#* เช่น ถ้าผู้ใช้ป้อน "p" และ chosen word เป็น "apple" display ควรจะเป็น ["_", "p", "p", "_", "_"].
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

#TODO-3: - แสดง 'display' และดูว่าตัวที่เดาถูกตำแหน่ง และตัวอื่นยังคงเป็น "_".

