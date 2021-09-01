import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - สร้าง List ว่าง และตั้งชื่อว่า display.
#* ให้เพิ่ม '_' ใน list display เท่ากับจำนวนตัวอักษรใน chosen_word
#* เช่น หาก chosen_word เป็น "apple", display จะเป็น ["_", "_", "_", "_", "_"]
display = []
word_len = len(chosen_word)
for i in range(word_len):
    display.append('_')

#guess = input("Guess a letter: ").lower()
guess = 'o'

#TODO-2: - วน Loop ไปแต่ละตำแหน่งใน chosen_word
#* ถ้าตัวอักษรในตำแหน่งนั้นตรงกับ 'guess' ให้เปลี่ยนตัวอักษรใน display เป็น guess ในตำแหน่งเดียวกัน
#* เช่น ถ้าผู้ใช้ป้อน "p" และ chosen word เป็น "apple" display ควรจะเป็น ["_", "p", "p", "_", "_"].
for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

#TODO-3: - แสดง 'display' และดูว่าตัวที่เดาถูกตำแหน่ง และตัวอื่นยังคงเป็น "_".
print (display)
