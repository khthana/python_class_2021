#-----------------------------------------
#* Game of Rock Paper Scissors
#-----------------------------------------

#TODO-1: ให้ import random
import random

#TODO-2: รับ Input ว่าเป็น rock, paper, scissors
user_action = input("Enter a choice (rock, paper, scissors): ")

#TODO-3: สร้าง List ของ rock, paper, scissors และให้คอมพิวเตอร์สุ่มเลือก
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

#TODO-4: แสดงผลว่าผู้เล่นเลือกอะไร และ คอมพิวเตอร์เลือกอะไร 
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
