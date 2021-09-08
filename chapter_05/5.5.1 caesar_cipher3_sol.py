#---------------------------------------------------
#* จากโปรแกรมที่เขียน จะพบว่าฟังก์ชัน encrypt และ decrypt
#* มีความคล้ายคลึงกันมาก
#* ดังนั้นควรจะรวมทั้ง 2 ฟังก์ชันให้เป็นอันเดียว
#---------------------------------------------------

#| Ex 5.9 จากโปรแกรมต่อไปนี้ ให้รวมฟังก์ชัน encrypt และ decrypt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: รวมฟังก์ชัน encrypt() และ decrypt() เป็นฟังก์ชันเดียวชื่อว่า caesar(). 
"""
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")
"""

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")


#TODO-2: ทดลองเรียกใช้ caesar() โดยส่งข้อความ 'text' จำนวนที่เลื่อน 'shift' และ 'direction' 
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
