from enum import IntEnum
import random

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

#TODO-1: สร้างฟังก์ชัน get_user_selection()
#|       ให้รับ Input จากคีย์บอร์ด แล้วให้ส่งคืนเป็น Action 
#|       แก้ปัญหาการกดผิดของ User 
#|       ในการรับจาก User ให้รับ 0,1,2 แทนการป้อน string 

# def get_user_selection():
#     user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
#     selection = int(user_input)
#     action = Action(selection)
#     return action

#TODO-2: ให้ปรับปรุงฟังก์ชัน get_user_selection() ให้ใช้ list comprehension
def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

#TODO-3: สร้างฟังก์ชัน get_computer_selection(): โดยทำคล้ายกับ user_selection
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

#TODO-4: สร้างฟังก์ชัน determine_winner(user_action, computer_action)
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

#TODO-5: แก้ไข loop while ให้เรียกใช้ฟังก์ชัน ที่เขียนขึ้นข้างต้น

while True:
    user_action = get_user_selection()
    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
