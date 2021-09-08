#---------------------------------------------------
#* ในสมัยโรมัน มีการส่งข้อมูลแบบเข้ารหัส เพื่อป้องกันการอ่านแอบอ่าน
#* เรียกว่าการเข้ารหัสแบบซีซาร์ โดยใช้วิธีการเลื่อนตัวอักษร
#* abcdefghijklmnopqrstuvwxyz
#* เช่น ถ้ากำหนดเลื่อน 5 ข้อความ hello -> mkrru
#* กรณีที่เป็นตัว z จะวนกลับไปใช้ abc ใหม่
#---------------------------------------------------

#| Ex 5.7 จากโปรแกรมต่อไปนี้ จงเขียนโปรแกรมในจุดที่ระบุ TODO 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: สร้าง function ชื่อ 'encrypt' ที่รับข้อมูล 'text' และ 'shift' เป็น Input
def encrypt(plain_text, shift_amount):

    #TODO-2: ในฟังก์ชัน 'encrypt' ให้ทำการ shift แต่ละตัวอักษรของ 'text' ไปข้างหน้า
    #|       เท่ากับจำนวนที่ระบุใน 'shift' และ print ผลลัพธ์ที่เข้ารหัสแล้ว 
    #|       สามารถหาตำแหน่งได้โดยใช้ list.index(element)
    #| e.g. 
    #| plain_text = "hello"
    #| shift = 5
    #| cipher_text = "mjqqt"
    #| print output: "The encoded text is mjqqt"
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

    #*HINT: How do you get the index of an item in a list:
    #*https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    #!🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: เรียกใช้ฟังก์ชัน encrypt โดยรับข้อมูล 2 ตัว คือ text และ shift และทดสอบ
encrypt(plain_text=text, shift_amount=shift)