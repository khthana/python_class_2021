#------------------------------------------------------------------
#* จงเขียนโปรแกรมทายตัวเลข ระหว่าง 1-99 โดยโปรแกรมตอบว่า 
#* มากไป (Too high) หรือ น้อยไป (Too low) และแสดง Guess again.
#* ถ้าตอบถูก ให้แสดง "You got it! The answer was x."
#* ในการเล่นแต่ละรอบ ให้แสดงจำนวนครั้งที่เหลืออยู่ "You've x attempts remaining."
#* ถ้าครบแล้วให้แสดง "You've run out of guesses, you lose."
#* โปรแกรมมี 2 โหมดการทำงานให้เลือก คือ โหมดยาก (5 ครั้ง) และ โหมดง่าย (10 ครั้ง)
#*
#* ตอนเริ่มโปรแกรมให้แสดงข้อความ "Welcome to the Number Guessing Game!"
#-------------------------------------------------------------------
from random import randint

#| Step 1 : กำหนดลำดับงาน
#|          - คอมพิวเตอร์สุ่มเลือกตัวเลข 1-99 
#|          - ให้เลือกโหมดยาก หรือง่าย
#|          - ผู้ใช้เลือกตัวเลข
#|          - ตรวจสอบว่าถูกหรือไม่ 
#|          - ถ้าถูกแสดงว่าถูกและจบเกม ถ้าไม่ถูกให้ลดจำนวนการทาย -1 
#|          - วนกลับไปทำลำดับที่ 3 

#| Step 2 : เลือกงานที่นำมาเขียนเป็น functionได้
#|          - เลือกโหมดยากหรือง่าย
#|          - ตรวจคำตอบว่าถูกหรือไม่

#| Step 3 : เขียน fn : เลือกโหมด และทดสอบ
#|          พารามิเตอร์ : ไม่มี
#|          การส่งกลับ : จำนวนครั้งที่ให้ทาย

# ถ้าจะให้โปรแกรมสวย ให้กำหนดเป็นตัวแปร เพื่อใช้ return 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5

#| Step 4 : เขียน fn : ตรวจคำตอบว่าถูกหรือไม่
#|          พารามิเตอร์ : ตัวเลขที่ทาย, คำตอบ, จำนวนครั้งคงเหลือ 
#|          การส่งกลับ : จำนวนครั้งคงเหลือ -1 
#|          การทำงานย่อย : 
#|              ถ้าตัวเลขที่ทาย > คำตอบ แสดง Too high.
#|              ถ้าตัวเลขที่ทาย < คำตอบ แสดง Too low.
#|              else แสดง You got it! The answer was answer

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#| Step 5: เขียน ฟังก์ชันหลัก

print("Welcome to the Number Guessing Game!")
answer = randint(1, 99)
print(f"Pssst, the correct answer is {answer}") 

turns = set_difficulty()

guess = 0
while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #ผู้ใช้ทายตัวเลข 
    guess = int(input("Make a guess: "))

    #ตรวจสอบว่าถูกต้องหรือไม่ 
    turns = check_answer(guess, answer, turns)

    if turns == 0:
        print("You've run out of guesses, you lose.")
        break
    elif guess != answer:
        print("Guess again.")