
#| Ex 5.8 จากโปรแกรมต่อไปนี้ จงเขียนโปรแกรมในจุดที่ระบุ TODO 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: สร้างอีก 1 ฟังก์ชันชื่อว่า 'decrypt' โดยรับ 'text' และ 'shift' เป็น input.
def decrypt(cipher_text, shift_amount):

  #TODO-2: ในฟังก์ชัน 'decrypt' ให้ shift แต่ละตัวอักษรใน 'text' *ย้อนกลับ* ใน alphabet
  #|       เท่ากับจำนวน shift amount และพิมพ์ข้อความที่ถอดรหัสได้ออกมา
  #|e.g. 
  #|cipher_text = "mjqqt"
  #|shift = 5
  #|plain_text = "hello"
  #|print output: "The decoded text is hello"
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")


#TODO-3: ตรวจสอบว่าผู้ใช้ต้องการจะ encrypt หรือ decrypt ข้อความ
#|       โดยใช้ตัวแปร ชื่อ 'direction' และตรวจสอบจากตัวแปรนี้ในการเรียก encrypt หรือ decrypt

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)