alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
    #TODO-3: แก้ปัญหากรณีผู้ใช้ป้อน ตัวเลข เครื่องหมาย หรือ space
    #|เช่น start_text = "meet me at 3"
    #|      end_text = "•••• •• •• 3"

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: ให้ถาม user จะทำงานในโปรแกรมต่อหรือไม่
#|       ถ้าตอบ 'yes' ให้ทำงานต่อ ถ้าตอบ 'no' ให้หยุด
#|       ถ้าตอบ yes ให้ถาม direction/text/shift และเรียก caesar() อีกครั้ง
#|       hint : ใช้ while loop ช่วย
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#TODO-2: จะเกิดอะไรขึ้นถ้าผู้ใช้ ใส่ตัวเลข shift เกินจำนวนตัวอักษร เช่น 45 ให้แก้โปรแกรม
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")