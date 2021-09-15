from enum import IntEnum
import random

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

#TODO-1: ปรับปรุงฟังก์ชัน determine_winner โดยใช้ dictionary
#|    victories = {
#|        Action.Rock: [Action.Scissors],  # Rock beats scissors
#|        Action.Paper: [Action.Rock],  # Paper beats rock
#|        Action.Scissors: [Action.Paper]  # Scissors beats paper
#|    }

def determine_winner(user_action, computer_action):
    victories = {
        Action.Rock: [Action.Scissors],  # Rock beats scissors
        Action.Paper: [Action.Rock],  # Paper beats rock
        Action.Scissors: [Action.Paper]  # Scissors beats paper
    }

    defe2ats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")


while True:
    user_action = get_user_selection()
    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
