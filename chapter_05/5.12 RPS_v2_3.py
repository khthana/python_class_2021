#--------------------------------------------
#* โปรแกรมใน version ก่อนหน้านี้ มีปัญหาในการรับ string
#* ที่อาจจะสะกดผิด หรือ yes, y ตัวใหญ่ ตัวเล็ก
#* ดังนั้นจะใช้ library ที่ชื่อ IntEnum มาช่วย

from enum import IntEnum
import random

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

#* Action.Rock == Action(0)

#TODO-1: สร้างฟังก์ชัน get_user_selection()
#|       ให้รับ Input จากคีย์บอร์ด แล้วให้ส่งคืนเป็น Action 
#|       แก้ปัญหาการกดผิดของ User 
#|       ในการรับจาก User ให้รับ 0,1,2 แทนการป้อน string 

def get_user_selection():
    user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
    selection = int(user_input)
    action = Action(selection)
    return action

#TODO-2: ให้ปรับปรุงฟังก์ชัน get_user_selection() ให้ใช้ list comprehension

#TODO-3: สร้างฟังก์ชัน get_computer_selection(): โดยทำคล้ายกับ user_selection

#TODO-4: สร้างฟังก์ชัน determine_winner(user_action, computer_action)

#TODO-5: แก้ไข loop while ให้เรียกใช้ฟังก์ชัน ที่เขียนขึ้นข้างต้น

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


